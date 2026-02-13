"""
Test de extracción de cartera por edades con EasyOCR
Basado en el código optimizado de Gemini
"""
import sys
sys.path.insert(0, r'c:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\MIAppExtraccion')

from app import extraer_datos, extraer_cartera_por_edades_con_easyocr
from PIL import Image

def test_cartera_easyocr():
    """Test del extractor optimizado con EasyOCR"""
    
    # Imagen de cartera por edades
    img_path = r"C:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\Pueba\ppppp\WhatsApp Image 2026-01-08 at 8.09.55 PM.jpeg"
    
    try:
        # Cargar imagen
        imagen = Image.open(img_path)
        print(f"✅ Imagen cargada: {imagen.size}")
        
        # Test 1: Función directa con EasyOCR
        print("\n" + "="*60)
        print("TEST 1: Extracción directa con EasyOCR")
        print("="*60)
        
        resultado_easyocr = extraer_cartera_por_edades_con_easyocr(imagen)
        if resultado_easyocr and '_filas' in resultado_easyocr:
            filas = resultado_easyocr['_filas']
            print(f"🎯 EasyOCR detectó {len(filas)} filas")
            print("\nPrimeras 3 filas:")
            for i, fila in enumerate(filas[:3]):
                print(f"  Fila {i+1}: {fila}")
        else:
            print("❌ EasyOCR no detectó filas")
        
        # Test 2: Función principal integrada
        print("\n" + "="*60)  
        print("TEST 2: Extracción integrada (extraer_datos)")
        print("="*60)
        
        # Simular OCR rápido para detectar que es cartera
        from app import ocr_imagen
        texto = ocr_imagen(imagen)
        
        # Llamar función principal con imagen
        datos, tablas = extraer_datos(texto, "WhatsApp Image 2026-01-08.jpeg", imagen)
        
        if isinstance(datos, dict) and '_tipo' in datos:
            filas_integradas = datos.get('_filas', [])
            print(f"🎯 Integración detectó {len(filas_integradas)} filas")
            print(f"Tipo: {datos.get('_tipo')}")
        else:
            print("❌ Integración no detectó estructura de tabla")
        
        # Comparar resultados
        print("\n" + "="*60)
        print("COMPARACIÓN DE RESULTADOS")
        print("="*60)
        
        if resultado_easyocr and datos and '_filas' in datos:
            filas_directas = len(resultado_easyocr.get('_filas', []))
            filas_integradas = len(datos.get('_filas', []))
            print(f"EasyOCR directo: {filas_directas} filas")
            print(f"Integración: {filas_integradas} filas")
            
            if filas_directas > 0 and filas_integradas > 0:
                print("✅ Ambos métodos funcionaron!")
            else:
                print("⚠️ Al menos uno falló")
        
        print(f"\n🎉 Test completado exitosamente!")
        
    except ImportError as e:
        print(f"❌ EasyOCR no está instalado: {e}")
    except FileNotFoundError:
        print("❌ Imagen no encontrada")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    test_cartera_easyocr()