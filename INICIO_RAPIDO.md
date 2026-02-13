# 🚀 INICIO RÁPIDO - 60 SEGUNDOS

## ⚡ La Forma Más Rápida de Empezar

### 1️⃣ Ejecutar la Aplicación

**Windows:**
```cmd
EJECUTAR_APP.bat
```

**PowerShell:**
```powershell
.\EJECUTAR_APP.ps1
```

Se abrirá automáticamente en: `http://localhost:8501`

---

## 📱 Primeros Pasos en la Interfaz

1. **Cargar documento** → Arrastra o selecciona archivo (PDF/Imagen)

2. **Elegir estrategia:**
   - **AUTO** ← Recomendado para empezar
   - **RAPIDO** ← Si necesitas velocidad
   - **AZURE** ← Máxima precisión (ya configurado ✅)

3. **Click en "EXTRAER DATOS"**

4. **Ver resultados** → Pestaña "Datos Extraídos"

5. **Descargar** → Botón "Descargar CSV/Excel/JSON"

---

## 🎯 Casos de Uso Rápidos

### Factura Simple
```
Estrategia: RAPIDO
Tiempo: 1-2 segundos
Precisión: ⭐⭐⭐
```

### Tabla de Cartera
```
Estrategia: BALANCEADO
Tiempo: 3-5 segundos
Precisión: ⭐⭐⭐⭐
```

### Documento Escaneado
```
Estrategia: AZURE
Tiempo: 2-4 segundos
Precisión: ⭐⭐⭐⭐⭐
```

### Comparar Opciones
```
Estrategia: COMPARAR
Tiempo: 15-25 segundos
Resultado: Tabla comparativa de todos los métodos
```

---

## 🔥 Atajos de Teclado

Una vez en la interfaz:

- **Ctrl + R** → Rerun (actualizar)
- **Ctrl + C** → Cerrar servidor
- **F11** → Pantalla completa

---

## 🆘 Problemas Comunes

### "Tesseract no encontrado"
```bash
# Descargar e instalar desde:
https://github.com/UB-Mannheim/tesseract/wiki
```

### "Azure no disponible"
Ya está configurado ✅ Si tienes problemas:
```bash
python config.py
```

### "Streamlit command not found"
```bash
pip install streamlit
```

---

## 📊 Ejemplo de Uso Programático

Si prefieres código Python:

```python
from extractor_maestro import extraer_documento

# Extracción con selección automática
datos, tiempo = extraer_documento("factura.jpg", estrategia="AUTO")

print(f"Extraído en {tiempo:.2f}s")
for campo, valor in datos.items():
    if not campo.startswith('_'):
        print(f"{campo}: {valor}")
```

---

## 💡 Siguiente Nivel

Una vez que domines lo básico:

1. **Lee:** [README_SISTEMA_INTEGRADO.md](README_SISTEMA_INTEGRADO.md)
2. **Explora:** Pestaña "Comparar Métodos"
3. **Aprende:** Sistema de auto-aprendizaje en sidebar
4. **Optimiza:** Usa Azure para documentos críticos

---

## 🎉 ¡Listo!

Ahora solo:

```bash
streamlit run app_maestro.py
```

**¡Y empieza a extraer datos! 🚀**

---

## 🔗 Enlaces Útiles

- **Guía Completa:** [README_SISTEMA_INTEGRADO.md](README_SISTEMA_INTEGRADO.md)
- **Setup Azure:** [README_AZURE.md](README_AZURE.md)
- **Ayuda Git:** [GUIA_GITHUB.md](GUIA_GITHUB.md)

---

**⏱️ Tiempo total de lectura: 60 segundos**

**⏱️ Tiempo hasta primera extracción: 2 minutos**

**¡Happy Extracting! 🎯**
