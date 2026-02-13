"""
🚀 EXTRACTOR MAESTRO - SISTEMA INTEGRADO DE EXTRACCIÓN
========================================================
Combina todas las herramientas disponibles:
- OCR Local: Tesseract, EasyOCR, PaddleOCR
- Azure Document Intelligence (Cloud)
- Auto-aprendizaje con FuzzyWuzzy y Pydantic
- Extracción de tablas con img2table y coordenadas
- Memoria persistente

Estrategias disponibles:
1. RAPIDO: Solo Tesseract (más rápido, menos preciso)
2. BALANCEADO: Tesseract + PaddleOCR para tablas
3. PRECISO: EasyOCR + PaddleOCR (más lento, más preciso)
4. AZURE: Azure Document Intelligence (requiere conexión + credenciales)
5. COMPARAR: Ejecuta múltiples métodos y compara resultados
6. AUTO: Selección inteligente según tipo de documento
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Union
import time
from io import BytesIO
from PIL import Image
import pandas as pd

# Importar módulos locales
try:
    from app import (
        ocr_imagen, 
        ocr_pdf_bytes, 
        extraer_datos,
        extraer_tabla_con_easyocr,
        cargar_memoria,
        guardar_memoria
    )
except ImportError as e:
    print(f"⚠️  Error importando app.py: {e}")
    sys.exit(1)

# Importar Azure (opcional)
AZURE_DISPONIBLE = False
try:
    from config import AZURE_ENDPOINT, AZURE_KEY
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.formrecognizer import DocumentAnalysisClient
    AZURE_DISPONIBLE = True
except ImportError:
    print("ℹ️  Azure Document Intelligence no disponible (falta instalación o config.py)")


class ExtractorMaestro:
    """
    Clase unificada para extracción de documentos con múltiples estrategias
    """
    
    def __init__(self):
        self.memoria = cargar_memoria()
        self.azure_client = None
        
        # Inicializar cliente Azure si está disponible
        if AZURE_DISPONIBLE and AZURE_ENDPOINT and AZURE_KEY:
            try:
                self.azure_client = DocumentAnalysisClient(
                    endpoint=AZURE_ENDPOINT,
                    credential=AzureKeyCredential(AZURE_KEY)
                )
                print("✅ Cliente Azure Document Intelligence inicializado")
            except Exception as e:
                print(f"⚠️  Error inicializando Azure: {e}")
    
    def extraer_con_tesseract(self, imagen: Image.Image) -> Tuple[Dict, float]:
        """
        Extracción rápida con Tesseract
        Retorna: (datos_extraidos, tiempo_segundos)
        """
        inicio = time.time()
        texto = ocr_imagen(imagen)
        resultado = extraer_datos(texto)
        
        # Manejar tupla si extraer_datos retorna (datos, tablas)
        if isinstance(resultado, tuple):
            datos, _ = resultado
        else:
            datos = resultado
            
        tiempo = time.time() - inicio
        return datos, tiempo
    
    def extraer_con_paddleocr(self, imagen: Image.Image) -> Tuple[Dict, float]:
        """
        Extracción con PaddleOCR para tablas complejas
        Retorna: (datos_extraidos, tiempo_segundos)
        """
        inicio = time.time()
        
        try:
            # Usar extracción de tablas con coordenadas
            tabla = extraer_tabla_con_easyocr(imagen, columnas_esperadas=8)
            datos = {
                "_tipo": "tabla_paddle",
                "_filas": tabla if tabla else [],
                "_metodo": "PaddleOCR"
            }
        except Exception as e:
            print(f"⚠️  Error en PaddleOCR: {e}")
            # Fallback a Tesseract
            return self.extraer_con_tesseract(imagen)
        
        tiempo = time.time() - inicio
        return datos, tiempo
    
    def extraer_con_easyocr(self, imagen: Image.Image) -> Tuple[Dict, float]:
        """
        Extracción precisa con EasyOCR
        Retorna: (datos_extraidos, tiempo_segundos)
        """
        inicio = time.time()
        
        try:
            import easyocr
            reader = easyocr.Reader(['es', 'en'], gpu=False)
            
            # Convertir PIL a array numpy
            import numpy as np
            img_array = np.array(imagen)
            
            resultados = reader.readtext(img_array)
            texto = "\n".join([texto for (bbox, texto, confianza) in resultados])
            
            resultado = extraer_datos(texto)
            if isinstance(resultado, tuple):
                datos, _ = resultado
            else:
                datos = resultado
                
        except Exception as e:
            print(f"⚠️  Error en EasyOCR: {e}")
            return self.extraer_con_tesseract(imagen)
        
        tiempo = time.time() - inicio
        return datos, tiempo
    
    def extraer_con_azure(self, imagen: Image.Image) -> Tuple[Dict, float]:
        """
        Extracción de alta precisión con Azure Document Intelligence
        Retorna: (datos_extraidos, tiempo_segundos)
        """
        if not self.azure_client:
            print("⚠️  Azure no está disponible. Usando Tesseract.")
            return self.extraer_con_tesseract(imagen)
        
        inicio = time.time()
        
        try:
            # Convertir imagen a bytes
            img_byte_arr = BytesIO()
            imagen.save(img_byte_arr, format='PNG')
            img_byte_arr.seek(0)
            
            # Analizar documento
            poller = self.azure_client.begin_analyze_document(
                "prebuilt-layout", 
                document=img_byte_arr
            )
            result = poller.result()
            
            # Extraer datos
            datos = {"_metodo": "Azure Document Intelligence"}
            
            # Extraer pares clave-valor
            if result.key_value_pairs:
                for kv_pair in result.key_value_pairs:
                    if kv_pair.key and kv_pair.value:
                        key = kv_pair.key.content.strip()
                        value = kv_pair.value.content.strip()
                        datos[key] = value
            
            # Extraer tablas
            if result.tables:
                tablas_extraidas = []
                for tabla in result.tables:
                    filas = {}
                    for celda in tabla.cells:
                        fila_idx = celda.row_index
                        if fila_idx not in filas:
                            filas[fila_idx] = {}
                        filas[fila_idx][celda.column_index] = celda.content
                    
                    # Convertir a lista de listas
                    tabla_lista = []
                    for idx in sorted(filas.keys()):
                        fila = filas[idx]
                        fila_ordenada = [fila.get(col_idx, "") for col_idx in range(tabla.column_count)]
                        tabla_lista.append(fila_ordenada)
                    
                    tablas_extraidas.append(tabla_lista)
                
                datos["_tablas_azure"] = tablas_extraidas
                datos["_tipo"] = "documento_azure"
            
        except Exception as e:
            print(f"⚠️  Error en Azure: {e}")
            return self.extraer_con_tesseract(imagen)
        
        tiempo = time.time() - inicio
        return datos, tiempo
    
    def extraer_balanceado(self, imagen: Image.Image) -> Tuple[Dict, float]:
        """
        Estrategia balanceada: Tesseract para texto + PaddleOCR para tablas
        """
        inicio = time.time()
        
        # Paso 1: Extracción rápida con Tesseract
        texto = ocr_imagen(imagen)
        resultado = extraer_datos(texto)
        
        if isinstance(resultado, tuple):
            datos, _ = resultado
        else:
            datos = resultado
        
        # Paso 2: Si parece tener tabla, usar PaddleOCR
        if self._parece_tener_tabla(texto):
            try:
                tabla = extraer_tabla_con_easyocr(imagen, columnas_esperadas=8)
                if tabla:
                    datos["_tabla_paddle"] = tabla
                    datos["_metodo"] = "Balanceado (Tesseract + PaddleOCR)"
            except Exception as e:
                print(f"⚠️  PaddleOCR falló: {e}")
        
        tiempo = time.time() - inicio
        return datos, tiempo
    
    def extraer_auto(self, imagen: Image.Image, nombre_archivo: str = "") -> Tuple[Dict, float]:
        """
        Selección automática del mejor método según características del documento
        """
        inicio = time.time()
        
        # Análisis rápido con Tesseract
        texto = ocr_imagen(imagen)
        
        # Decisión inteligente
        if self._es_cartera_clientes(texto):
            # Documento de cartera → PaddleOCR (tablas)
            print("🔍 Detectado: Cartera de clientes → Usando PaddleOCR")
            datos, _ = self.extraer_con_paddleocr(imagen)
            
        elif self._es_formula_medica(texto):
            # Fórmula médica → Tesseract (texto estructurado)
            print("🔍 Detectado: Fórmula médica → Usando Tesseract")
            resultado = extraer_datos(texto)
            datos = resultado[0] if isinstance(resultado, tuple) else resultado
            
        elif self._es_documento_complejo(texto):
            # Documento complejo → Azure (si disponible) o EasyOCR
            if self.azure_client:
                print("🔍 Detectado: Documento complejo → Usando Azure")
                datos, _ = self.extraer_con_azure(imagen)
            else:
                print("🔍 Detectado: Documento complejo → Usando EasyOCR")
                datos, _ = self.extraer_con_easyocr(imagen)
        else:
            # Documento estándar → Balanceado
            print("🔍 Detectado: Documento estándar → Usando modo balanceado")
            datos, _ = self.extraer_balanceado(imagen)
        
        tiempo = time.time() - inicio
        datos["_metodo_auto"] = "Selección automática"
        return datos, tiempo
    
    def comparar_metodos(self, imagen: Image.Image) -> Dict[str, Tuple[Dict, float]]:
        """
        Ejecuta múltiples métodos y retorna comparación
        Retorna: {"tesseract": (datos, tiempo), "paddle": (datos, tiempo), ...}
        """
        print("\n🔬 COMPARANDO MÉTODOS DE EXTRACCIÓN...")
        print("=" * 60)
        
        resultados = {}
        
        # Tesseract
        print("\n⏱️  Ejecutando Tesseract...")
        resultados["tesseract"] = self.extraer_con_tesseract(imagen)
        print(f"   ✅ Completado en {resultados['tesseract'][1]:.2f}s")
        
        # PaddleOCR
        print("\n⏱️  Ejecutando PaddleOCR...")
        resultados["paddleocr"] = self.extraer_con_paddleocr(imagen)
        print(f"   ✅ Completado en {resultados['paddleocr'][1]:.2f}s")
        
        # EasyOCR
        print("\n⏱️  Ejecutando EasyOCR...")
        resultados["easyocr"] = self.extraer_con_easyocr(imagen)
        print(f"   ✅ Completado en {resultados['easyocr'][1]:.2f}s")
        
        # Azure (si disponible)
        if self.azure_client:
            print("\n⏱️  Ejecutando Azure Document Intelligence...")
            resultados["azure"] = self.extraer_con_azure(imagen)
            print(f"   ✅ Completado en {resultados['azure'][1]:.2f}s")
        
        print("\n" + "=" * 60)
        print("✅ COMPARACIÓN COMPLETADA\n")
        
        return resultados
    
    # ============================================
    # MÉTODOS DE DETECCIÓN
    # ============================================
    
    def _parece_tener_tabla(self, texto: str) -> bool:
        """Detecta si el texto parece contener una tabla"""
        lineas = texto.split('\n')
        # Si hay muchas líneas con números y símbolos, probablemente es tabla
        lineas_numericas = sum(1 for linea in lineas if any(c.isdigit() for c in linea))
        return lineas_numericas > 5
    
    def _es_cartera_clientes(self, texto: str) -> bool:
        """Detecta si es un documento de cartera de clientes"""
        palabras_clave = ['cartera', 'cliente', 'saldo', 'vencido', 'corriente', 'mora']
        texto_lower = texto.lower()
        return sum(palabra in texto_lower for palabra in palabras_clave) >= 3
    
    def _es_formula_medica(self, texto: str) -> bool:
        """Detecta si es una fórmula médica"""
        palabras_clave = ['formula', 'médica', 'medica', 'medicamento', 'posología', 'dosis']
        texto_lower = texto.lower()
        return sum(palabra in texto_lower for palabra in palabras_clave) >= 2
    
    def _es_documento_complejo(self, texto: str) -> bool:
        """Detecta si es un documento complejo que requiere alta precisión"""
        # Documentos largos o con estructura compleja
        return len(texto) > 2000 or texto.count('\n') > 50


def extraer_documento(
    ruta_o_imagen: Union[str, Path, Image.Image],
    estrategia: str = "AUTO",
    comparar: bool = False
) -> Union[Tuple[Dict, float], Dict[str, Tuple[Dict, float]]]:
    """
    Función principal de extracción
    
    Args:
        ruta_o_imagen: Ruta al archivo o imagen PIL
        estrategia: "RAPIDO", "BALANCEADO", "PRECISO", "AZURE", "AUTO"
        comparar: Si True, ejecuta y compara múltiples métodos
    
    Returns:
        Si comparar=False: (datos_extraidos, tiempo_segundos)
        Si comparar=True: {"metodo": (datos, tiempo), ...}
    """
    
    # Cargar imagen
    if isinstance(ruta_o_imagen, (str, Path)):
        imagen = Image.open(ruta_o_imagen)
        nombre = Path(ruta_o_imagen).name
    else:
        imagen = ruta_o_imagen
        nombre = "imagen_sin_nombre.jpg"
    
    # Crear extractor
    extractor = ExtractorMaestro()
    
    # Modo comparación
    if comparar:
        return extractor.comparar_metodos(imagen)
    
    # Seleccionar estrategia
    estrategia = estrategia.upper()
    
    if estrategia == "RAPIDO":
        return extractor.extraer_con_tesseract(imagen)
    elif estrategia == "BALANCEADO":
        return extractor.extraer_balanceado(imagen)
    elif estrategia == "PRECISO":
        return extractor.extraer_con_easyocr(imagen)
    elif estrategia == "AZURE":
        return extractor.extraer_con_azure(imagen)
    elif estrategia == "AUTO":
        return extractor.extraer_auto(imagen, nombre)
    else:
        print(f"⚠️  Estrategia '{estrategia}' no reconocida. Usando AUTO.")
        return extractor.extraer_auto(imagen, nombre)


# ============================================
# FUNCIÓN DE UTILIDAD PARA EXPORTAR
# ============================================

def exportar_comparacion_excel(resultados: Dict[str, Tuple[Dict, float]], ruta_salida: str = "comparacion_metodos.xlsx"):
    """
    Exporta resultados de comparación a Excel
    """
    try:
        with pd.ExcelWriter(ruta_salida, engine='openpyxl') as writer:
            # Hoja de resumen
            resumen = []
            for metodo, (datos, tiempo) in resultados.items():
                campos_extraidos = len([k for k in datos.keys() if not k.startswith('_')])
                resumen.append({
                    'Método': metodo.upper(),
                    'Tiempo (seg)': round(tiempo, 2),
                    'Campos Extraídos': campos_extraidos
                })
            
            df_resumen = pd.DataFrame(resumen)
            df_resumen.to_excel(writer, sheet_name='Resumen', index=False)
            
            # Hoja por cada método
            for metodo, (datos, tiempo) in resultados.items():
                datos_limpios = {k: v for k, v in datos.items() if not k.startswith('_')}
                df = pd.DataFrame(list(datos_limpios.items()), columns=['Campo', 'Valor'])
                df.to_excel(writer, sheet_name=metodo.upper()[:31], index=False)
        
        print(f"✅ Comparación exportada a: {ruta_salida}")
        
    except Exception as e:
        print(f"⚠️  Error exportando: {e}")


# ============================================
# EJEMPLO DE USO
# ============================================

if __name__ == "__main__":
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║   🚀 EXTRACTOR MAESTRO - SISTEMA INTEGRADO                ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    # Ejemplo 1: Extracción con estrategia AUTO
    print("\n📌 EJEMPLO 1: Extracción Automática")
    print("-" * 60)
    
    ruta_ejemplo = "WhatsApp Image 2026-01-08 at 8.09.55 PM.jpg"
    
    if os.path.exists(ruta_ejemplo):
        datos, tiempo = extraer_documento(ruta_ejemplo, estrategia="AUTO")
        print(f"\n✅ Extracción completada en {tiempo:.2f} segundos")
        print(f"📊 Campos extraídos: {len(datos)}")
        
        # Mostrar primeros 5 campos
        print("\n🔍 Primeros campos:")
        for i, (k, v) in enumerate(list(datos.items())[:5]):
            print(f"   {k}: {v}")
    else:
        print(f"⚠️  Archivo no encontrado: {ruta_ejemplo}")
    
    # Ejemplo 2: Comparación de métodos
    print("\n\n📌 EJEMPLO 2: Comparación de Métodos")
    print("-" * 60)
    print("Para comparar métodos, usar:")
    print("   resultados = extraer_documento('imagen.jpg', comparar=True)")
    print("   exportar_comparacion_excel(resultados)")
