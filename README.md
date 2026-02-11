# 📄 Extractor Inteligente de Documentos

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Sistema de análisis automatizado de documentos con tecnología OCR. Extrae información clave de PDFs e imágenes de forma inteligente y la organiza en categorías para exportación.

![Demo](https://via.placeholder.com/800x400/667eea/ffffff?text=Extractor+Inteligente+de+Documentos)

## ✨ Características

- 🔍 **OCR Inteligente**: Extrae texto de PDFs e imágenes usando Tesseract
- 🎯 **Detección Automática**: Identifica fechas, nombres, cédulas, direcciones, valores monetarios y más
- 📊 **Organización por Categorías**: Clasifica la información extraída automáticamente
- 💾 **Exportación Flexible**: Descarga los datos en formato CSV o Excel
- 🎨 **Interfaz Moderna**: Diseño profesional con gradientes y animaciones
- 🌐 **Soporte Multiidioma**: OCR en español e inglés

## 🚀 Tipos de Documentos Soportados

- ✅ Resoluciones y licencias
- ✅ Contratos y acuerdos
- ✅ Facturas y recibos
- ✅ Certificados y documentos legales
- ✅ Cualquier imagen o PDF con texto

## 📋 Requisitos Previos

### Software Necesario

1. **Python 3.8 o superior**
   - [Descargar Python](https://www.python.org/downloads/)

2. **Tesseract OCR**
   - **Windows**: [Descargar instalador](https://github.com/UB-Mannheim/tesseract/wiki)
   - **Linux**: `sudo apt-get install tesseract-ocr tesseract-ocr-spa`
   - **macOS**: `brew install tesseract tesseract-lang`

3. **Poppler** (solo para PDFs en Windows)
   - [Descargar Poppler](https://github.com/oschwartz10612/poppler-windows/releases/)
   - Agregar a las variables de entorno PATH

## 🔧 Instalación

### Opción 1: Instalación Automática (Windows)

1. Clona el repositorio:
```bash
git clone https://github.com/TU_USUARIO/extractor-documentos.git
cd extractor-documentos
```

2. Ejecuta el script de instalación:
```bash
.\EJECUTAR_APP.bat
```

### Opción 2: Instalación Manual

1. Clona el repositorio:
```bash
git clone https://github.com/TU_USUARIO/extractor-documentos.git
cd extractor-documentos
```

2. Crea un entorno virtual:
```bash
python -m venv venv
```

3. Activa el entorno virtual:
   - **Windows**: `venv\Scripts\activate`
   - **Linux/macOS**: `source venv/bin/activate`

4. Instala las dependencias:
```bash
pip install -r requirements_app.txt
```

5. Configura Tesseract (ajusta la ruta si es necesario):
   - Edita `app_extractor_v3.py` línea 11:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

## 🎮 Uso

### Iniciar la Aplicación

```bash
streamlit run app_extractor_v3.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

### Uso Paso a Paso

1. **Cargar Documento**: Arrastra o selecciona un PDF o imagen
2. **Configurar OCR**: Ajusta DPI y número de páginas (sidebar)
3. **Procesar**: Haz clic en "PROCESAR DOCUMENTO"
4. **Revisar Datos**: Explora la información extraída organizada por categorías
5. **Exportar**: Selecciona los campos deseados y descarga en CSV o Excel

## 📊 Categorías de Extracción

El sistema identifica y organiza automáticamente:

| Categoría | Ejemplos |
|-----------|----------|
| 📅 Fechas | `12/01/2024`, `15 de marzo de 2024` |
| 📄 Documentos | Resoluciones, radicados, números de referencia |
| 🆔 Identificaciones | Cédulas, NITs |
| 👤 Nombres | Personas mencionadas en el documento |
| 📍 Ubicaciones | Direcciones, ciudades, municipios |
| 📞 Contactos | Teléfonos, emails |
| 💰 Valores | Montos en pesos, áreas en m², cantidades |
| 📋 Estados | Aprobado, negado, pendiente |

## ⚙️ Configuración Avanzada

### Ajustar Calidad OCR

En el sidebar de la aplicación:
- **DPI**: 100-150 (óptimo), 200-300 (alta calidad, más lento)
- **Páginas**: 1-2 (rápido), 3-5 (completo)

### Modificar Patrones de Extracción

Edita la función `extraer_datos()` en `app_extractor_v3.py` para agregar patrones personalizados usando expresiones regulares.

## 🌐 Despliegue en la Nube

### Streamlit Cloud (Gratis)

1. Sube tu código a GitHub
2. Ve a [share.streamlit.io](https://share.streamlit.io/)
3. Conecta tu repositorio
4. Configura:
   - **Main file**: `app_extractor_v3.py`
   - **Python version**: 3.9
5. Haz clic en "Deploy"

**Nota**: En Streamlit Cloud, el archivo `packages.txt` instalará automáticamente Tesseract.

## 📁 Estructura del Proyecto

```
extractor-documentos/
│
├── app_extractor_v3.py          # Aplicación principal
├── requirements_app.txt         # Dependencias Python
├── packages.txt                 # Dependencias del sistema (Streamlit Cloud)
├── .gitignore                   # Archivos ignorados por Git
├── README.md                    # Este archivo
│
├── .streamlit/
│   └── config.toml             # Configuración de Streamlit
│
└── EJECUTAR_APP.bat            # Script de inicio rápido (Windows)
```

## 🛠️ Solución de Problemas

### Tesseract no encontrado
```
Error: Tesseract not found
```
**Solución**: Verifica que Tesseract esté instalado y la ruta sea correcta en `app_extractor_v3.py`

### Error de idioma español
```
Error: Failed loading language 'spa'
```
**Solución**: 
1. Descarga `spa.traineddata` desde [tessdata](https://github.com/tesseract-ocr/tessdata/raw/main/spa.traineddata)
2. Copia el archivo a `C:\Program Files\Tesseract-OCR\tessdata\`

### PDF no se procesa
```
Error: Unable to open PDF
```
**Solución**: Instala Poppler (Windows) o verifica que `poppler-utils` esté instalado (Linux)

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor:

1. Haz un Fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👥 Autores

- **Soluciones V&G** - *Desarrollo inicial*

## 🙏 Agradecimientos

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Streamlit](https://streamlit.io/)
- [pdf2image](https://github.com/Belval/pdf2image)

## 📧 Soporte

¿Tienes preguntas? Abre un [issue](https://github.com/TU_USUARIO/extractor-documentos/issues) en GitHub.

---

⭐ Si este proyecto te fue útil, ¡dale una estrella en GitHub!
