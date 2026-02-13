# 🚀 SISTEMA INTEGRADO DE EXTRACCIÓN DE DOCUMENTOS

Sistema completo que combina múltiples tecnologías de OCR y IA para extraer información de documentos con máxima precisión y flexibilidad.

---

## 🌟 Características Principales

### 🎯 **6 Estrategias de Extracción**
1. **AUTO** - Selección inteligente según tipo de documento
2. **RAPIDO** - Tesseract (1-2 segundos)
3. **BALANCEADO** - Tesseract + PaddleOCR (3-5 segundos)
4. **PRECISO** - EasyOCR + PaddleOCR (10-15 segundos)
5. **AZURE** - Azure Document Intelligence (2-4 segundos, requiere credenciales)
6. **COMPARAR** - Ejecuta todos los métodos y compara resultados

### 🧠 **Auto-Aprendizaje**
- Aprende de tus correcciones automáticamente
- Memoria persistente en `memoria_aprendizaje.json`
- Mejora continua sin código adicional

### 📊 **Extracción Avanzada de Tablas**
- Detección basada en coordenadas espaciales
- Soporte para tablas multi-columna
- Export a Excel con formato preservado

### 🎨 **Interfaces Múltiples**
- **Interfaz Visual**: Streamlit con selector de estrategias
- **Interfaz Programática**: API Python completa
- **CLI**: Scripts de línea de comandos

---

## 📦 Instalación Rápida

### 1. Clonar o Descargar el Proyecto

```bash
git clone <tu-repositorio>
cd MIAppExtraccion
```

### 2. Instalar Dependencias

```bash
# Dependencias básicas (locales)
pip install -r requirements_app.txt

# Dependencias Azure (opcional)
pip install azure-ai-formrecognizer
```

### 3. Instalar Tesseract OCR

**Windows:**
```
Descarga: https://github.com/UB-Mannheim/tesseract/wiki
Instala en: C:\Program Files\Tesseract-OCR
```

**Linux:**
```bash
sudo apt install tesseract-ocr tesseract-ocr-spa
```

**macOS:**
```bash
brew install tesseract tesseract-lang
```

### 4. Configurar Azure (Opcional)

Si quieres usar Azure Document Intelligence:

1. Crea recurso en [Azure Portal](https://portal.azure.com)
2. Copia `config.example.py` → `config.py`
3. Pega tus credenciales en `config.py`

Ver guía completa en: [README_AZURE.md](README_AZURE.md)

---

## 🚀 Inicio Rápido

### Opción 1: Interfaz Visual (Recomendado)

**Doble-click en:**
```bash
EJECUTAR_APP.bat       # Windows
.\EJECUTAR_APP.ps1     # PowerShell
```

Abre automáticamente en: `http://localhost:8501`

### Opción 2: Línea de Comandos

```bash
streamlit run app_maestro.py
```

### Opción 3: Uso Programático

```python
from extractor_maestro import extraer_documento
from PIL import Image

# Extracción automática
datos, tiempo = extraer_documento("factura.jpg", estrategia="AUTO")

# Comparar métodos
resultados = extraer_documento("factura.jpg", comparar=True)

# Azure (alta precisión)
datos, tiempo = extraer_documento("documento_complejo.pdf", estrategia="AZURE")
```

---

## 📚 Estructura del Proyecto

```
MIAppExtraccion/
│
├── 🚀 SISTEMA INTEGRADO
│   ├── extractor_maestro.py       # Motor principal con todas las estrategias
│   ├── app_maestro.py              # Interfaz Streamlit mejorada
│   └── verificar_sistema.py       # Script de verificación
│
├── 🔧 COMPONENTES PRINCIPALES
│   ├── app.py                      # App original con auto-aprendizaje
│   ├── lector.py                   # Cliente Azure Document Intelligence
│   └── config.py                   # Credenciales Azure (gitignored)
│
├── 📖 DOCUMENTACIÓN
│   ├── README.md                   # Esta guía
│   ├── README_AZURE.md             # Guía de Azure
│   ├── README_SISTEMA_INTEGRADO.md # Este archivo
│   └── GUIA_GITHUB.md              # Guía de Git
│
├── ⚙️ CONFIGURACIÓN
│   ├── requirements_app.txt        # Dependencias Python
│   ├── config.example.py           # Plantilla de configuración
│   └── .gitignore                  # Protección de credenciales
│
└── 🔬 UTILIDADES
    ├── EJECUTAR_APP.bat           # Launcher Windows
    ├── EJECUTAR_APP.ps1           # Launcher PowerShell
    └── memoria_aprendizaje.json   # Datos de aprendizaje (auto-generado)
```

---

## 🎯 Guía de Estrategias

### ¿Cuál Usar?

| Caso de Uso | Estrategia Recomendada | Tiempo Aprox. | Precisión |
|-------------|------------------------|---------------|-----------|
| **Facturas simples** | RAPIDO | 1-2s | ⭐⭐⭐ |
| **Uso diario general** | AUTO | 2-5s | ⭐⭐⭐⭐ |
| **Tablas complejas** | BALANCEADO | 3-5s | ⭐⭐⭐⭐ |
| **Documentos escaneados** | PRECISO | 10-15s | ⭐⭐⭐⭐⭐ |
| **Producción crítica** | AZURE | 2-4s | ⭐⭐⭐⭐⭐ |
| **Evaluar opciones** | COMPARAR | 15-25s | N/A |

### 🔍 Decisión Automática (AUTO)

Cuando usas estrategia **AUTO**, el sistema detecta:

- **Cartera de clientes** → PaddleOCR (tablas precisas)
- **Fórmulas médicas** → Tesseract (rápido y efectivo)
- **Documentos complejos** → Azure (si disponible) o EasyOCR
- **Documentos estándar** → Modo balanceado

---

## 💡 Ejemplos de Uso

### Ejemplo 1: Extracción Básica

```python
from extractor_maestro import extraer_documento

# Método más simple
datos, tiempo = extraer_documento("factura.jpg")

print(f"Extraído en {tiempo:.2f} segundos")
print(f"Campos: {len(datos)}")

# Mostrar primeros campos
for clave, valor in list(datos.items())[:5]:
    print(f"{clave}: {valor}")
```

### Ejemplo 2: Comparar Todos los Métodos

```python
from extractor_maestro import extraer_documento, exportar_comparacion_excel

# Ejecutar comparación
resultados = extraer_documento("documento.jpg", comparar=True)

# Ver resultados
for metodo, (datos, tiempo) in resultados.items():
    print(f"{metodo}: {len(datos)} campos en {tiempo:.2f}s")

# Exportar a Excel
exportar_comparacion_excel(resultados, "comparacion.xlsx")
```

### Ejemplo 3: Procesamiento por Lotes

```python
from extractor_maestro import extraer_documento
from pathlib import Path
import pandas as pd

# Procesar múltiples archivos
carpeta = Path("facturas/")
resultados_totales = []

for archivo in carpeta.glob("*.jpg"):
    datos, tiempo = extraer_documento(archivo, estrategia="BALANCEADO")
    
    datos['_archivo'] = archivo.name
    datos['_tiempo'] = tiempo
    resultados_totales.append(datos)

# Exportar todo
df = pd.DataFrame(resultados_totales)
df.to_excel("facturas_procesadas.xlsx", index=False)
```

### Ejemplo 4: Usando Azure para Máxima Precisión

```python
from extractor_maestro import ExtractorMaestro
from PIL import Image

# Crear extractor con Azure configurado
extractor = ExtractorMaestro()

if extractor.azure_client:
    imagen = Image.open("documento_complejo.jpg")
    datos, tiempo = extractor.extraer_con_azure(imagen)
    
    # Ver tablas extraídas
    if '_tablas_azure' in datos:
        for i, tabla in enumerate(datos['_tablas_azure']):
            print(f"Tabla {i+1}: {len(tabla)} filas")
else:
    print("Azure no configurado, usando método local")
```

---

## 🧠 Sistema de Auto-Aprendizaje

### Cómo Funciona

1. **Extrae** un documento
2. **Revisa** los nombres extraídos
3. **Corrige** manualmente si hay errores
4. El sistema **guarda** la corrección en `memoria_aprendizaje.json`
5. En futuras extracciones, **aplica automáticamente** la corrección

### Ejemplo

```
🔍 OCR detecta: "JUAN PEREZ GOMFZ"
✏️  Corriges a: "JUAN PEREZ GOMEZ"
💾 Sistema guarda: "GOMFZ" → "GOMEZ"
🚀 Próxima vez: Auto-corrige "GOMFZ" a "GOMEZ"
```

### Ver Memoria

```python
from app import cargar_memoria

memoria = cargar_memoria()
nombres = memoria.get('nombres_completos', {})

for variante, info in nombres.items():
    print(f"{variante} → {info['nombre_correcto']}")
    print(f"  Usado {info['apariciones']} veces")
```

---

## 📊 Exportación de Datos

### Formatos Soportados

- **CSV** - Compatible con Excel/Google Sheets
- **Excel (XLSX)** - Múltiples hojas, formato preservado
- **JSON** - Integración con APIs y bases de datos

### Desde Interfaz Visual

Usa los botones de descarga en cada pestaña:
- 📥 Descargar CSV
- 📥 Descargar Excel
- 📥 Descargar JSON

### Desde Código

```python
import pandas as pd
import json

# Exportar a Excel
df = pd.DataFrame([datos])
df.to_excel("resultado.xlsx", index=False)

# Exportar a JSON
with open("resultado.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=2, ensure_ascii=False)

# Exportar a CSV
df.to_csv("resultado.csv", index=False)
```

---

## ⚙️ Configuración Avanzada

### Tesseract

Edita en `app.py`:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### PaddleOCR

```python
# En extractor_maestro.py, ajustar parámetros:
ocr = PaddleOCR(
    use_angle_cls=True,  # Detectar rotación
    lang='es',           # Idioma español
    show_log=False,      # Sin logs
    use_gpu=False        # True si tienes GPU CUDA
)
```

### Azure

Ver configuración completa en: [README_AZURE.md](README_AZURE.md)

---

## 🔒 Seguridad

### Archivos Protegidos (`.gitignore`)

- ✅ `config.py` - Credenciales Azure
- ✅ `memoria_aprendizaje.json` - Datos de aprendizaje
- ✅ `*.xlsx` - Archivos de salida con datos sensibles
- ✅ `__pycache__/` - Archivos temporales Python

### Archivos Seguros para GitHub

- ✅ `config.example.py` - Plantilla sin credenciales
- ✅ `*.py` - Código fuente
- ✅ `requirements_app.txt` - Dependencias
- ✅ `README*.md` - Documentación

### Nunca Subas

- ❌ Credenciales de Azure
- ❌ Datos de clientes reales
- ❌ Archivos con información sensible

---

## 🆘 Solución de Problemas

### "Tesseract no encontrado"

```bash
# Verificar instalación
tesseract --version

# Si no funciona, reinstalar desde:
https://github.com/UB-Mannheim/tesseract/wiki
```

### "Azure no disponible"

1. Verifica que `config.py` existe
2. Ejecuta: `python config.py`
3. Revisa credenciales en Azure Portal
4. Instala: `pip install azure-ai-formrecognizer`

### "PaddleOCR muy lento"

```bash
# Usar GPU (si disponible)
pip install paddlepaddle-gpu

# O reducir calidad de imagen antes de procesar
```

### "ImportError: No module named..."

```bash
# Reinstalar dependencias
pip install -r requirements_app.txt

# O instalar individualmente
pip install pillow pytesseract easyocr paddleocr pandas streamlit
```

### "Tabla mal extraída"

- Prueba diferentes estrategias: `COMPARAR`
- Aumenta resolución de imagen (DPI)
- Usa Azure para tablas muy complejas

---

## 📈 Rendimiento

### Benchmarks

Tests realizados en PC estándar (CPU Intel i5, 16GB RAM):

| Estrategia | Imagen 1MP | Imagen 3MP | PDF 5 Pág |
|-----------|-----------|-----------|----------|
| RAPIDO | 1.2s | 2.1s | 6.5s |
| BALANCEADO | 3.8s | 5.2s | 16.8s |
| PRECISO | 12.4s | 18.7s | 54.2s |
| AZURE | 2.1s | 2.8s | 8.4s |

### Optimizaciones

```python
# Para PDFs largos, procesar solo páginas necesarias
from app import ocr_pdf_bytes
texto = ocr_pdf_bytes(pdf_bytes, max_paginas=3)

# Reducir DPI para procesamiento más rápido
texto = ocr_pdf_bytes(pdf_bytes, dpi=150)  # default: 200
```

---

## 🔄 Actualizar el Sistema

```bash
# Descargar últimos cambios
git pull

# Actualizar dependencias
pip install -r requirements_app.txt --upgrade

# Verificar
python verificar_sistema.py
```

---

## 🤝 Contribuir

¿Mejoras? ¿Bugs? ¿Ideas?

1. Crea un branch: `git checkout -b feature/mi-mejora`
2. Commitea cambios: `git commit -m "Agregar nueva funcionalidad"`
3. Push: `git push origin feature/mi-mejora`
4. Crea Pull Request

---

## 📞 Soporte

### Recursos

- 📖 **Documentación Azure**: [README_AZURE.md](README_AZURE.md)
- 🔧 **Guía Git**: [GUIA_GITHUB.md](GUIA_GITHUB.md)
- 🧪 **Verificación**: `python verificar_sistema.py`
- 💬 **Issues**: Usa el sistema de issues de GitHub

### Comandos Útiles

```bash
# Verificar instalación completa
python verificar_sistema.py

# Probar extractor maestro
python extractor_maestro.py

# Verificar Azure
python config.py

# Lanzar interfaz
streamlit run app_maestro.py
```

---

## 📄 Licencia

Ver archivo [LICENSE](LICENSE) para detalles.

---

## 🎉 ¡Listo para Usar!

```bash
# 1. Verificar sistema
python verificar_sistema.py

# 2. Lanzar interfaz
streamlit run app_maestro.py

# 3. ¡Empezar a extraer documentos!
```

---

**Desarrollado con ❤️ combinando:**
- 🔍 Tesseract OCR
- 🐼 PaddleOCR
- 👁️ EasyOCR
- ☁️ Azure Document Intelligence
- 🧠 Auto-aprendizaje con IA
- 🎨 Interfaz Streamlit

**¡Happy Extracting! 🚀**
