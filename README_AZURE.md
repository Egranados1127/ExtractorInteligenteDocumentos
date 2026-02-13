# 🔐 Configuración de Azure Document Intelligence

Este proyecto incluye soporte para **Azure Document Intelligence** (Form Recognizer) para extracción de tablas con alta precisión.

## 📋 Archivos de Configuración

### `config.py` (PRIVADO - NO SUBIR A GITHUB)
Contiene tus credenciales reales de Azure. Este archivo **está protegido** en `.gitignore`.

### `config.example.py` (PÚBLICO)
Plantilla de ejemplo que sí puede subirse a GitHub como referencia.

### `lector.py`
Script que usa Azure Document Intelligence para extraer tablas de imágenes.

---

## 🚀 Guía de Configuración

### **Paso 1: Crear Recurso en Azure**

1. Ve a [Azure Portal](https://portal.azure.com)
2. Crea un nuevo recurso **"Document Intelligence"**
3. Espera a que se complete el despliegue
4. Haz clic en "Go to resource"

### **Paso 2: Obtener Credenciales**

1. En tu recurso, ve a **"Keys and Endpoint"**
2. Copia:
   - **Endpoint**: URL como `https://tu-recurso.cognitiveservices.azure.com/`
   - **Key 1**: Cadena alfanumérica de ~32 caracteres

### **Paso 3: Configurar config.py**

1. Abre `config.py`
2. Reemplaza los valores:

```python
AZURE_ENDPOINT = "https://tu-recurso-REAL.cognitiveservices.azure.com/"
AZURE_KEY = "tu-clave-real-de-32-caracteres"
RUTA_IMAGEN = "WhatsApp Image 2026-01-08 at 8.09.55 PM.jpg"
```

### **Paso 4: Instalar Dependencias**

```bash
pip install azure-ai-formrecognizer pandas openpyxl
```

### **Paso 5: Verificar Configuración**

```bash
python config.py
```

Debes ver:
```
✅ Configuración OK
📍 Endpoint: https://...
🔑 Key configurada: a1b2c3d4e5...f6g7
📄 Imagen: WhatsApp Image...
```

### **Paso 6: Ejecutar Extracción**

```bash
python lector.py
```

Resultado:
```
✅ Credenciales cargadas desde config.py
Analizando documento... por favor espera.
¡Listo! Se ha creado el archivo 'Cartera_Extraida.xlsx'.
```

---

## 💰 Costos y Límites

### **Nivel Gratuito (F0)**
- ✅ **500 páginas/mes** gratis
- ✅ Sin tarjeta de crédito requerida (en algunos planes)
- ✅ Ideal para desarrollo y pruebas

### **Nivel Pago (S0)**
- 💵 Desde $1.50 USD por 1,000 páginas
- 💡 Solo pagas lo que usas
- 🚀 Sin límites de volumen

### **Recomendación**
Comienza con el nivel **F0** (gratuito) para probar. Escala a **S0** solo si necesitas procesar más de 500 páginas al mes.

---

## 🔒 Seguridad

### ✅ **Archivos Protegidos** (en `.gitignore`)
- `config.py` - Tus credenciales reales
- `memoria_aprendizaje.json` - Datos de aprendizaje
- `Cartera_Extraida.xlsx` - Salidas con datos sensibles

### ⚠️ **NUNCA Subas a GitHub:**
- Endpoints
- Keys/Claves
- Datos de clientes
- Archivos de salida con información real

### ✅ **Sí Puedes Subir:**
- `config.example.py` - Plantilla sin datos reales
- `lector.py` - Código fuente
- Este README

---

## 🆚 Comparación: Azure vs Soluciones Locales

| Característica | Azure Doc Intelligence | PaddleOCR/EasyOCR |
|----------------|------------------------|-------------------|
| **Precisión en Tablas** | ⭐⭐⭐⭐⭐ Excelente | ⭐⭐⭐ Buena |
| **Detección Auto de Estructura** | ✅ Sí | ⚠️ Manual |
| **Requiere Internet** | ✅ Sí | ❌ No |
| **Costo** | 💰 Pago (500 pág gratis/mes) | 🆓 Gratis |
| **Configuración** | 🔧 Más compleja | ⚡ Simple |
| **Documentos Escaneados** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Velocidad** | ⚡⚡⚡⚡ Rápida (en nube) | ⚡⚡ Depende de hardware |

### **¿Cuándo Usar Cada Uno?**

**Usa Azure si:**
- ✅ Necesitas máxima precisión
- ✅ Procesas tablas complejas
- ✅ Tienes presupuesto disponible
- ✅ Requieres soporte empresarial

**Usa PaddleOCR/EasyOCR si:**
- ✅ Quieres solución 100% gratuita
- ✅ Necesitas trabajar offline
- ✅ Tienes control sobre calidad de imágenes
- ✅ Volumen bajo de documentos

---

## 🆘 Solución de Problemas

### Error: "Endpoint no configurado"
```
⚠️ ERROR: Debes configurar AZURE_ENDPOINT en config.py
```
**Solución**: Edita `config.py` con tu endpoint real de Azure.

### Error: "Unauthorized" o "401"
**Causas:**
- Key incorrecta
- Endpoint incorrecto
- Recurso eliminado en Azure

**Solución**: Verifica credenciales en Azure Portal.

### Error: "ImportError: No module named 'azure.ai.formrecognizer'"
```bash
pip install azure-ai-formrecognizer
```

### Imagen No Se Procesa
**Verifica:**
1. Ruta correcta en `RUTA_IMAGEN`
2. Archivo existe
3. Formato soportado (JPG, PNG, PDF, TIFF)

---

## 📚 Recursos Adicionales

- [Documentación Oficial de Azure Document Intelligence](https://learn.microsoft.com/es-es/azure/ai-services/document-intelligence/)
- [Precios Actualizados](https://azure.microsoft.com/es-es/pricing/details/ai-document-intelligence/)
- [Guía de Inicio Rápido](https://learn.microsoft.com/es-es/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api)

---

## 📧 Soporte

Si tienes problemas:
1. Verifica que `config.py` esté correctamente configurado
2. Ejecuta `python config.py` para validar
3. Revisa que tu recurso Azure esté activo
4. Consulta los logs de error completos

---

**¡Tu configuración está protegida! 🔒**
Gracias al `.gitignore`, tus credenciales nunca se subirán accidentalmente a GitHub.
