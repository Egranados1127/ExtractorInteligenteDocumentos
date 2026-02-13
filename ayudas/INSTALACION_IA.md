# 🤖 Guía de Instalación - Extracción con IA

Esta guía te ayudará a configurar las funcionalidades avanzadas de inteligencia artificial para la extracción de datos.

---

## 📋 ¿Qué hay de nuevo?

La aplicación ahora incluye **3 métodos de extracción**:

### 1. 📌 Extracción por Patrones (Original)
- Busca usando expresiones regulares
- Campos predefinidos: Fechas, Cédulas, NITs, etc.

### 2. 🔍 Extracción Automática de Pares Clave-Valor (NUEVO)
- Detecta automáticamente patrones como:
  - `Nombre del Proyecto: Casa Verde`
  - `Beneficiario: Juan Pérez`
  - `Presupuesto | $5,000,000`
- **No requiere instalación adicional**
- Los campos extraídos tienen prefijo `Auto_`

### 3. 🤖 Extracción con IA - NER (NUEVO)
- Usa inteligencia artificial para identificar:
  - Personas
  - Lugares
  - Organizaciones
  - Otras entidades
- **Requiere instalación de modelo de español**
- Los campos extraídos tienen prefijo `IA_`

---

## ⚙️ Instalación Paso a Paso

### **Paso 1: Instalar Dependencias Base**

Abre PowerShell en la carpeta del proyecto y ejecuta:

```powershell
pip install -r requirements_app.txt
```

Esto instalará:
- ✅ Streamlit
- ✅ Pandas
- ✅ Pillow
- ✅ pytesseract
- ✅ pdf2image
- ✅ openpyxl
- ✅ spaCy (librería base)

---

### **Paso 2: Instalar Modelo de Español para IA**

Tenemos **2 opciones**:

#### **Opción A: Script Automático (Recomendado)** 🎯

Ejecuta el script de instalación:

```powershell
python setup_spacy.py
```

Este script:
1. Verifica que spaCy esté instalado
2. Descarga e instala el modelo de español
3. Verifica la instalación

#### **Opción B: Instalación Manual**

Si prefieres hacerlo manualmente:

```powershell
python -m spacy download es_core_news_sm
```

---

### **Paso 3: Verificar Instalación**

Ejecuta este comando para verificar:

```powershell
python -c "import spacy; nlp = spacy.load('es_core_news_sm'); print('✅ Todo listo!')"
```

Si ves `✅ Todo listo!` significa que la instalación fue exitosa.

---

## 🚀 Nuevas Funcionalidades

### **1. Modo de Carga Múltiple**

Ahora puedes procesar documentos de 3 formas:

#### 📄 **Archivo Individual**
- Sube un documento a la vez
- Ideal para revisión detallada

#### 📄📄 **Múltiples Archivos**
- Selecciona varios archivos (Ctrl + Click)
- Procesamiento en batch
- Tabla comparativa

#### 📁 **Carpeta ZIP**
- Comprime tus documentos en un .zip
- Sube el archivo
- Procesa todo automáticamente

---

### **2. Resultados Mejorados**

#### **Vista Consolidada**
- Tabla con todos los archivos procesados
- Compara datos entre documentos
- Scroll horizontal para ver todos los campos

#### **Documentos Individuales**
- Selector para revisar cada documento
- Datos organizados por categorías:
  - 📌 Datos Automáticos (pares clave-valor)
  - 🤖 Entidades IA (personas, lugares, etc.)
  - 📅 Fechas
  - 👤 Nombres
  - 📍 Ubicaciones
  - Y más...

#### **Exportación Avanzada**
- **CSV Simple**: Tabla en texto plano
- **Excel Simple**: Una hoja con todo consolidado
- **Excel Completo**: 
  - Hoja "Consolidado" con resumen
  - Una hoja por cada documento
  - Perfecto para análisis detallado

---

### **3. Filtrado Inteligente**

- ✅ Checkbox para cada campo
- ✅ Selecciona solo lo que necesitas
- ✅ Export personalizado
- ✅ Vista previa antes de descargar

---

## 📊 Ejemplo de Uso

### **Caso: Procesar 10 Resoluciones**

**Antes:**
1. Subir archivo 1
2. Procesar
3. Descargar CSV
4. Subir archivo 2
5. Procesar
6. Descargar CSV
7. ... (repetir 10 veces)
8. Consolidar manualmente en Excel

**Ahora:**
1. Comprimir las 10 resoluciones en `resoluciones.zip`
2. Seleccionar modo "Carpeta ZIP"
3. Subir archivo
4. Click en "PROCESAR CARPETA ZIP"
5. Ver tabla consolidada
6. Seleccionar campos deseados
7. Descargar Excel completo con todo

**Resultado:** De 30 minutos a **2 minutos** ⚡

---

## 🎯 Comparación de Métodos

| Característica | Patrones | Auto Clave-Valor | IA NER |
|----------------|----------|------------------|---------|
| Instalación | ✅ Base | ✅ Base | ⚙️ Modelo español |
| Velocidad | ⚡⚡⚡ | ⚡⚡⚡ | ⚡⚡ |
| Precisión | Alta para patrones conocidos | Alta si formato es consistente | Alta para entidades |
| Flexibilidad | Baja | Media | Alta |
| Campos | Predefinidos | Dinámicos | Dinámicos |

**Recomendación:** Usa los **3 métodos juntos** para máxima cobertura.

---

## ⚠️ Solución de Problemas

### **Error: "Model 'es_core_news_sm' not found"**

**Solución:**
```powershell
python setup_spacy.py
```

O manualmente:
```powershell
python -m spacy download es_core_news_sm
```

---

### **Error: "No module named 'spacy'"**

**Solución:**
```powershell
pip install spacy
```

---

### **La extracción con IA no funciona**

La aplicación seguirá funcionando normalmente con los otros 2 métodos. Si el modelo de español no está instalado:
- ✅ Extracción por patrones: Funciona
- ✅ Extracción automática: Funciona
- ❌ Extracción con IA: Se omite silenciosamente

**Para activar IA:** Instala el modelo con `python setup_spacy.py`

---

### **Los archivos del ZIP no se procesan**

Verifica:
1. El ZIP no tiene contraseña
2. Los archivos son PDF, PNG, JPG, JPEG o TIFF
3. Los archivos no están en subcarpetas profundas
4. El ZIP no supera 200 MB

---

## 📝 Próximos Pasos

1. ✅ Instala las dependencias
2. ✅ Ejecuta `python setup_spacy.py`
3. ✅ Ejecuta la app: `streamlit run app.py`
4. ✅ Prueba con un documento
5. ✅ Prueba con múltiples archivos
6. ✅ Prueba con un ZIP

---

## 🆘 Soporte

Si tienes problemas:

1. Revisa esta guía completa
2. Verifica que Tesseract OCR esté instalado
3. Asegúrate de tener todas las dependencias
4. Ejecuta `python setup_spacy.py` para verificar

---

## 📚 Recursos Adicionales

- **spaCy**: https://spacy.io/
- **Modelos de español**: https://spacy.io/models/es
- **Documentación Streamlit**: https://docs.streamlit.io/

---

**¡Disfruta la nueva versión con IA! 🚀**

*Desarrollado por Soluciones V&G*
