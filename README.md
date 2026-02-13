# 📄 Extractor Inteligente de Documentos

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Sistema de análisis automatizado de documentos con tecnología OCR. Extrae información clave de PDFs e imágenes de forma inteligente y la organiza en categorías para exportación.

![Demo](https://via.placeholder.com/800x400/667eea/ffffff?text=Extractor+Inteligente+de+Documentos)

## 📱 **NUEVO: MOBILE-FIRST & CAPTURA DE CÁMARA** 🚀

**¡Tu app ahora funciona en CUALQUIER dispositivo y puede capturar fotos directamente!**

### 🎯 **Características Mobile:**
- 📸 **Captura directa con cámara** - Toma fotos desde smartphones, tablets o PC
- 📱 **Diseño 100% responsive** - Se adapta automáticamente a móviles, tablets y desktop
- 👆 **Optimizado para touch** - Botones grandes y táctiles (mínimo 44px)
- 🌐 **Acceso remoto** - Usa la app desde cualquier lugar con conexión
- ⚡ **Sin necesidad de archivos** - Captura → Procesa → Descarga en un solo flujo

### 📷 **Cómo usar desde móvil:**
1. Ejecuta: `.\EJECUTAR_APP.ps1` en tu PC
2. Abre la URL local en tu móvil: `http://192.168.X.X:8501`
3. Selecciona **"📷 Capturar Foto"**
4. Apunta al documento y captura
5. ¡Listo! Descarga el Excel directamente

📖 **[Ver guía completa de características mobile](MOBILE_FEATURES.md)**

---

## ✨ Características

### 🎯 Extracción Inteligente (5 Métodos)

1. **📌 Extracción por Patrones**
   - Campos predefinidos usando regex
   - Alta precisión para formatos conocidos

2. **🏥 Extractores Especializados** ✨ NUEVO
   - **HERINCO**: Entregas de medicamentos (27 campos específicos)
   - **Vision Integrados**: Fórmulas médicas (33 campos con reconstrucción de texto)
   - **Tablas de Ventas**: Múltiples filas con PPTO, valores y márgenes
   - **Tablas de 2 Columnas**: NOMBRE RUT | NOMBRE COMERCIAL (N filas)
   - **Cartera por Edades**: Aging reports con 8 columnas (DOCUMENTO, PROVEEDOR, rangos de días, Total)

3. **🔍 Pares Clave-Valor Automáticos**
   - Detecta automáticamente "Etiqueta: Valor"
   - Campos dinámicos según tu documento
   - No requiere configuración

4. **🤖 Inteligencia Artificial (NER)**
   - Identifica personas, lugares, organizaciones
   - Reconocimiento contextual avanzado
   - Powered by spaCy

5. **📊 Tablas Múltiples** ✨ NUEVO
   - Extrae tablas completas con múltiples filas
   - Exportación directa a Excel/CSV
   - Formato automático de valores monetarios

### 📁 Procesamiento Múltiple ✨ NUEVO

- 📄 **Archivo Individual**: Procesa un documento a la vez
- 📄📄 **Múltiples Archivos**: Selecciona varios archivos (Ctrl+Click)
- � **Captura de Cámara**: Toma fotos directamente desde cualquier dispositivo (móvil, tablet, PC) ✨ NUEVO
- 📁 **Carpeta ZIP**: Sube una carpeta comprimida con todos tus documentos

### 💡 Otras Características

- 📱 **Mobile-First**: Diseño 100% responsive optimizado para smartphones y tablets ✨ NUEVO
- 📸 **Captura Directa**: Usa la cámara de tu dispositivo para procesar documentos físicos ✨ NUEVO
- 👆 **Touch Optimized**: Interfaz táctil con botones grandes (mínimo 44px) ✨ NUEVO

- 🔍 **OCR Inteligente**: Extrae texto de PDFs e imágenes usando Tesseract
- 🎯 **Detección Automática**: Identifica fechas, nombres, cédulas, direcciones, valores monetarios y más
- 📊 **Organización por Categorías**: Clasifica la información extraída automáticamente
- 💾 **Exportación Flexible**: CSV, Excel simple o Excel completo con pestañas
- 🎨 **Interfaz Moderna**: Diseño profesional con gradientes y animaciones
- 🌐 **Soporte Multiidioma**: OCR en español e inglés
- 📊 **Tabla Consolidada**: Compara datos de múltiples documentos
- ✅ **Filtrado Personalizado**: Selecciona qué campos exportar

## 🚀 Tipos de Documentos Soportados

### Documentos con Extractores Especializados ✨

- ✅ **HERINCO** - Entregas de medicamentos
  - 27 campos: DOCUMENTO, NOMBRES, FORMULA, ASEGURADORA, NIVEL, FECHA, VALOR CUOTA, CODIGO INTERNO, DIRECCION, TELEFONO, CELULAR, SEDE ENTREGA, CIUDAD, FECHA FORMULA, REGIMEN, CODIGO IPS, DESCRIPCION IPS, CODIGO MEDICO, NOMBRE MEDICO, CODIGO CIE, CONTRATO, COD ATC, NUA, NOMBRE GENERICO, CAN ENTR, CAN PEND, FORMULACION
  - Precisión: 100% (27/27 campos)

- ✅ **Vision Integrados** - Fórmulas médicas
  - 33 campos incluyendo medicamentos con reconstrucción inteligente de texto corrupto
  - Precisión: 97% (32/33 campos)

- ✅ **Tablas de Ventas** - Screenshots de WhatsApp con datos de asesores
  - 6 columnas: NOMBRE ASESOR, PPTO MES, PPTO A LA FECHA, VALOR VENTAS, % CUMPLIMIENTO, % MARGEN
  - Extracción de múltiples filas (hasta 20+ registros)
  - Formato automático de valores monetarios ($ 100.000.000)

- ✅ **Tablas de 2 Columnas** - Listas de empresas/RUTs
  - 2 columnas: NOMBRE RUT, NOMBRE COMERCIAL
  - Corrección automática de artefactos OCR ($ A S → S.A.S)
  - Precisión: 100% (20/20 filas en pruebas)

- ✅ **Cartera por Edades (Aging Report)** - Reportes de cuentas por cobrar ✨ NUEVO
  - 8 columnas: DOCUMENTO, PROVEEDOR, Corriente, De 1 a 30, De 31 a 60, De 61 a 90, De 91 o mas, Total
  - Extracción de múltiples proveedores (60+ filas)
  - Formato automático de valores monetarios
  - Lectura vertical de columnas (tabla girada en el OCR)

### Documentos Generales

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

5. **✨ NUEVO: Instala el modelo de IA para extracción avanzada** (Opcional pero recomendado)

   **Opción A - Script automático:**
   ```bash
   python setup_spacy.py
   ```
   
   **Opción B - Manual:**
   ```bash
   python -m spacy download es_core_news_sm
   ```
   
   **Opción C - Batch (Windows):**
   ```bash
   .\INSTALAR_SPACY.bat
   ```
   
   > 📝 **Nota:** Si no instalas el modelo de IA, la app funcionará normalmente pero sin la extracción con inteligencia artificial. Seguirás teniendo extracción por patrones y pares clave-valor automáticos.

6. Configura Tesseract (ajusta la ruta si es necesario):
   - Edita `app.py` línea ~17:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

## 🎮 Uso

### Iniciar la Aplicación

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

### ✨ Uso Paso a Paso - NUEVAS CARACTERÍSTICAS

#### **Modo 1: Archivo Individual**

1. Selecciona "📄 Archivo Individual"
2. Arrastra o selecciona un PDF o imagen
3. Ajusta DPI y número de páginas (sidebar)
4. Haz clic en "PROCESAR DOCUMENTO"
5. Revisa los datos extraídos en las 3 pestañas
6. Selecciona campos y exporta

#### **Modo 2: Múltiples Archivos** ✨ NUEVO

1. Selecciona "📄📄 Múltiples Archivos"
2. Selecciona varios archivos (Ctrl/Cmd + Click)
3. Haz clic en "PROCESAR TODOS LOS ARCHIVOS"
4. Espera el procesamiento batch
5. Revisa la **tabla consolidada** con todos los documentos
6. Navega por documentos individuales
7. Exporta en CSV, Excel simple o **Excel completo con pestañas**

#### **Modo 3: Carpeta ZIP** ✨ NUEVO

1. Comprime tus documentos en un archivo .zip
2. Selecciona "📁 Carpeta ZIP"
3. Sube el archivo ZIP
4. Haz clic en "PROCESAR CARPETA ZIP"
5. La app extrae y procesa todos los archivos automáticamente
6. Descarga el Excel consolidado con todos los resultados

### 🎯 Tipos de Datos Extraídos

La aplicación ahora extrae datos usando **3 métodos simultáneos**:

#### 1. **📌 Campos por Patrones** (Tradicional)
- Fechas, Cédulas, NITs
- Números de documento
- Teléfonos, emails
- Valores monetarios

#### 2. **🔍 Pares Automáticos** (Nuevo)
- Cualquier par "Etiqueta: Valor"
- Campos con prefijo `Auto_`
- Ejemplo: `Auto_Nombre_del_Proyecto`, `Auto_Beneficiario`

#### 3. **🤖 Entidades IA** (Nuevo - requiere modelo spaCy)
- Personas identificadas automáticamente
- Lugares y ubicaciones
- Organizaciones
- Campos con prefijo `IA_`
- Ejemplo: `IA_Persona_1`, `IA_Lugar_1`

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

## 🏥 Extractores Especializados - Ejemplos de Uso ✨ NUEVO

### HERINCO - Entrega de Medicamentos

**Entrada**: PDF de orden de entrega HERINCO  
**Salida**: 27 campos estructurados

```
DOCUMENTO: CC-39412449
NOMBRES: BEATRIZ ALICIA URREGO ORTIZ
FORMULA: 20251126
ASEGURADORA: SAVIA
NIVEL: 4
FECHA: 09/12/2025
VALOR CUOTA: 0
CODIGO INTERNO: 18773897
DIRECCION: CALLE 10 # 9-14 APTO 204
TELEFONO: 3287493
CELULAR: 3128459092
SEDE ENTREGA: VENTAS - CENTRO DIST. DOMICILIARA PROG.
CIUDAD: CAMPAMENTO
...
NOMBRE GENERICO: HIALURONATO DE SODIO 0.4% SOLUCION OFTALMICA
CAN ENTR: 1
CAN PEND: 0
FORMULACION: DURANTE 30 DIAS
```

### Vision Integrados - Fórmula Médica

**Entrada**: PDF de fórmula médica Vision Integrados  
**Salida**: 33 campos con reconstrucción inteligente

```
Código del Prestador: 800101439
Nit: 800.101.439-0
Paciente: BEATRIZ ALICIA URREGO ORTIZ
Identificacion: 39412449
Fecha Ingreso: 15/08/2025
Edad: 53 AÑOS
Sexo: F
Dx Principal: H048
Médico: DIANA CRISTINA ARANGO GUTIERREZ
Código: 22229
Descripción: HIALURONATO DE SODIO 0.4% SOLUCION OFTALMICA
Cantidad: 12
Posologia: APLICAR 1 GOTA CADA 8 HORAS EN AMBOS OJOS
Dias: 30
```

### Tabla de Ventas - Múltiples Filas

**Entrada**: Imagen WhatsApp con tabla de ventas  
**Salida**: DataFrame con N filas × 6 columnas

| NOMBRE ASESOR | PPTO MES | PPTO A LA FECHA | VALOR VENTAS | % CUMPLIMIENTO | % MARGEN |
|---------------|----------|-----------------|--------------|----------------|----------|
| SUROESTE | $ 100.000.000 | $ 100.000.000 | $ 103.733.005 | 100% | 24.65% |
| QUIROZ CASTRO LUIS ALEJANDRO | $ 100.000.000 | $ 100.000.000 | $ 101.380.349 | 101% | 24.11% |
| CALL CENTER | | | $ 11.540.853 | | 22.24% |
| ... | ... | ... | ... | ... | ... |
| TOTAL FIEL | $ 1.290.000.000 | $ 1.290.000.000 | $ 1.033.702.279 | 80% | 22.85% |

**Características**:
- ✅ Extracción de todas las filas automáticamente
- ✅ Formato de valores monetarios ($ 100.000.000)
- ✅ Exportación directa a Excel/CSV
- ✅ Manejo de filas incompletas (sin PPTO)

### Tabla de 2 Columnas - RUT y Nombre Comercial

**Entrada**: Imagen con tabla de ferreterías  
**Salida**: DataFrame con N filas × 2 columnas

| NOMBRE RUT | NOMBRE COMERCIAL |
|------------|------------------|
| FERRETERIA EL PORTILLO S.A.S | FERRETERIA EL PORTILLO S.A.S |
| HURTADO VILLADA MARIA FENY | ANYEP COMERCIAL |
| MORENO GARCIA CARLOS ALBERTO | FERRETERIA MORENO |
| ... | ... |

**Correcciones automáticas de OCR**:
- `(P))` → eliminado
- `*` → eliminado
- `$ A S` → `S.A.S`

### Cartera por Edades (Aging Report) - Múltiples Proveedores ✨ NUEVO

**Entrada**: Imagen WhatsApp con tabla de cartera por edades  
**Salida**: DataFrame con N filas × 8 columnas

| DOCUMENTO | PROVEEDOR | Corriente | De 1 a 30 | De 31 a 60 | De 61 a 90 | De 91 o mas | Total |
|-----------|-----------|-----------|-----------|------------|------------|-------------|--------|
| soDasosea | GRUPO EMPRESARIAL MERCURY SAS | $315.673.228 | $988.130.554 | $0 | $0 | $0 | $600.721.124 |
| 01504002 | ANDES CABLES SAS | $69.245.870 | $134.374.808 | $529.403.147 | $0 | $0 | $242.009.600 |
| 200033159 | DURMAN COLOMBIA SAS | $28.765.512 | $82.500.005 | $407.221.124 | $0 | $0 | $140.900.598 |
| ... | ... | ... | ... | ... | ... | ... | ... |

**Características**:
- ✅ Extracción de 60+ proveedores automáticamente
- ✅ 8 columnas: DOCUMENTO, PROVEEDOR + 6 columnas de valores
- ✅ Formato automático de valores monetarios
- ✅ Detección por palabra clave "PROVEEDOR"
- ✅ Lectura vertical de columnas (el OCR lee la tabla por columnas)

## ⚙️ Configuración Avanzada

### Ajustar Calidad OCR

En el sidebar de la aplicación:
- **DPI**: **200 (por defecto - recomendado)** ✨ NUEVO, 100-150 (rápido), 300 (máxima calidad, más lento)
- **Páginas**: 1-2 (rápido), 3-5 (completo)

> 💡 **Importante**: El DPI por defecto ahora es **200** en lugar de 100. Esto mejora significativamente la precisión de extracción para documentos HERINCO, Vision Integrados y tablas complejas.

### Exportación de Tablas Múltiples ✨ NUEVO

Cuando el sistema detecta un documento con múltiples filas (tablas):
- La pestaña "Datos Estructurados" muestra un DataFrame completo
- Botones de descarga directa para CSV y Excel
- Formato automático con separadores de miles en valores monetarios
- Todas las filas se exportan automáticamente (no hay selector de campos)

### Modificar Patrones de Extracción

Edita las funciones especializadas en `app.py`:
- `extraer_datos_herinco()` - Para documentos HERINCO
- `extraer_datos_vision_integrados()` - Para fórmulas Vision Integrados
- `extraer_tabla_ventas()` - Para tablas de ventas
- `extraer_tabla_dos_columnas()` - Para tablas de 2 columnas
- `extraer_cartera_por_edades()` - Para aging reports / cartera por edades ✨ NUEVO
- `extraer_datos()` - Para extracción genérica

## 🌐 Despliegue en la Nube

### Streamlit Cloud (Gratis)

1. Sube tu código a GitHub
2. Ve a [share.streamlit.io](https://share.streamlit.io/)
3. Conecta tu repositorio
4. Configura:
   - **Main file**: `app.py`
   - **Python version**: 3.9 o superior
5. Haz clic en "Deploy"

**Nota**: En Streamlit Cloud, el archivo `packages.txt` instalará automáticamente Tesseract.

> ⚠️ **Importante**: Los extractores especializados requieren DPI 200 para funcionar correctamente. Asegúrate de que Tesseract esté correctamente instalado en el servidor de Streamlit Cloud.

## 📁 Estructura del Proyecto

```
extractor-documentos/
│
├── app.py                       # Aplicación principal (Streamlit) ⭐
├── requirements_app.txt         # Dependencias Python
├── packages.txt                 # Dependencias del sistema (Streamlit Cloud)
├── .gitignore                   # Archivos ignorados por Git
├── README.md                    # Este archivo
├── LICENSE                      # Licencia MIT
│
├── EJECUTAR_APP.bat            # Script de inicio rápido (Windows)
├── EJECUTAR_APP.ps1            # Script PowerShell alternativo
├── GUIA_GITHUB.md              # Guía para usar Git y GitHub
│
└── .streamlit/
    └── config.toml             # Configuración de Streamlit

Extractores especializados en app.py:
- extraer_datos_herinco()           → 27 campos (entregas medicamentos)
- extraer_datos_vision_integrados() → 33 campos (fórmulas médicas)
- extraer_tabla_ventas()            → N filas × 6 columnas (tablas ventas)
- extraer_tabla_dos_columnas()      → N filas × 2 columnas (RUT/comercial)
- extraer_cartera_por_edades()      → N filas × 8 columnas (aging reports) ✨ NUEVO
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

### ✨ La extracción con IA no funciona

**Síntoma**: No aparecen campos con prefijo `IA_` en los resultados

**Solución**: 
1. El modelo de español de spaCy no está instalado
2. Ejecuta: `python setup_spacy.py`
3. O manualmente: `python -m spacy download es_core_news_sm`

📖 **Para más detalles**, consulta [INSTALACION_IA.md](INSTALACION_IA.md)

> **Nota**: La app funciona perfectamente sin el modelo de IA. Solo perderás la extracción de entidades con inteligencia artificial, pero seguirás teniendo extracción por patrones y pares clave-valor automáticos.

## 📚 Documentación Adicional

- 📖 [Guía de Instalación de IA](INSTALACION_IA.md) - Instalación completa de características avanzadas
- 📖 [Guía de GitHub](GUIA_GITHUB.md) - Cómo usar Git con este proyecto

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

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) - Motor de OCR
- [Streamlit](https://streamlit.io/) - Framework de interfaz web
- [pdf2image](https://github.com/Belval/pdf2image) - Conversión de PDF a imágenes
- [spaCy](https://spacy.io/) - Procesamiento de lenguaje natural e IA
- [Pandas](https://pandas.pydata.org/) - Análisis y manipulación de datos

## 📧 Soporte

¿Tienes preguntas? Abre un [issue](https://github.com/TU_USUARIO/extractor-documentos/issues) en GitHub.

---

⭐ Si este proyecto te fue útil, ¡dale una estrella en GitHub!
