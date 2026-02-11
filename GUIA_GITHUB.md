# 🚀 Guía de Publicación en GitHub

Esta guía te ayudará a publicar tu aplicación en GitHub paso a paso.

## 📋 Pre-requisitos

1. **Cuenta de GitHub**: [Crear cuenta](https://github.com/signup) si no tienes una
2. **Git instalado**: [Descargar Git](https://git-scm.com/downloads)
3. **GitHub Desktop (Opcional)**: [Descargar](https://desktop.github.com/) para interfaz gráfica

## 🔧 Opción 1: Usando Git desde la Terminal

### Paso 1: Configurar Git (Primera vez)

Abre PowerShell en la carpeta del proyecto y ejecuta:

```powershell
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email@example.com"
```

### Paso 2: Inicializar Repositorio Local

```powershell
cd "C:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\MIAppExtraccion"
git init
```

### Paso 3: Agregar Archivos al Repositorio

```powershell
git add .
git commit -m "Primera version: Extractor Inteligente de Documentos"
```

### Paso 4: Crear Repositorio en GitHub

1. Ve a [GitHub](https://github.com) e inicia sesión
2. Haz clic en el botón **"+"** (arriba derecha) → **"New repository"**
3. Configura:
   - **Repository name**: `extractor-documentos` (o el nombre que prefieras)
   - **Description**: "Sistema de análisis automatizado de documentos con OCR"
   - **Public** o **Private**: Elige según tus necesidades
   - **NO** marques "Add a README file" (ya lo tenemos)
   - Haz clic en **"Create repository"**

### Paso 5: Conectar y Subir al Repositorio Remoto

GitHub te mostrará comandos. Copia y pega en PowerShell:

```powershell
git remote add origin https://github.com/TU_USUARIO/extractor-documentos.git
git branch -M main
git push -u origin main
```

**Nota**: Reemplaza `TU_USUARIO` con tu nombre de usuario de GitHub.

Si te pide autenticación:
- **Usuario**: tu usuario de GitHub
- **Password**: usa un [Personal Access Token](https://github.com/settings/tokens) en lugar de tu contraseña

### Paso 6: Verificar

Ve a `https://github.com/TU_USUARIO/extractor-documentos` y verifica que todos los archivos estén ahí.

---

## 🖥️ Opción 2: Usando GitHub Desktop (Más Fácil)

### Paso 1: Instalar GitHub Desktop

1. Descarga e instala [GitHub Desktop](https://desktop.github.com/)
2. Inicia sesión con tu cuenta de GitHub

### Paso 2: Agregar el Proyecto

1. Abre GitHub Desktop
2. **File** → **Add local repository**
3. Selecciona la carpeta: `C:\Users\ediss\OneDrive - Soluciones V & G\Escritorio\MIAppExtraccion`
4. Si no está inicializado, haz clic en **"create a repository"**

### Paso 3: Hacer el Primer Commit

1. En la parte izquierda verás todos los archivos
2. En la parte inferior escribe:
   - **Summary**: "Primera version del extractor"
   - **Description** (opcional): Detalles adicionales
3. Haz clic en **"Commit to main"**

### Paso 4: Publicar en GitHub

1. Haz clic en **"Publish repository"** (arriba)
2. Configura:
   - **Name**: `extractor-documentos`
   - **Description**: "Sistema de análisis automatizado de documentos con OCR"
   - Marca o desmarca **"Keep this code private"** según prefieras
3. Haz clic en **"Publish repository"**

¡Listo! Tu proyecto ya está en GitHub.

---

## 🌐 (Opcional) Desplegar en Streamlit Cloud

### Paso 1: Ir a Streamlit Cloud

1. Ve a [share.streamlit.io](https://share.streamlit.io/)
2. Inicia sesión con tu cuenta de GitHub

### Paso 2: Crear Nueva App

1. Haz clic en **"New app"**
2. Configura:
   - **Repository**: Selecciona tu repo `extractor-documentos`
   - **Branch**: `main`
   - **Main file path**: `app_extractor_v3.py`
3. Haz clic en **"Deploy!"**

### Paso 3: Esperar Despliegue

- Toma 5-10 minutos la primera vez
- Streamlit Cloud instalará automáticamente:
  - Las dependencias de `requirements_app.txt`
  - Tesseract OCR y Poppler (desde `packages.txt`)

### Paso 4: Compartir la URL

Una vez desplegada, recibirás una URL como:
```
https://tu-usuario-extractor-documentos-abc123.streamlit.app
```

¡Comparte esta URL con quien quieras!

---

## 🔄 Actualizar el Proyecto

### Cuando hagas cambios:

**Con Git (Terminal)**:
```powershell
git add .
git commit -m "Descripcion de los cambios"
git push
```

**Con GitHub Desktop**:
1. Escribe el mensaje del commit
2. Haz clic en "Commit to main"
3. Haz clic en "Push origin"

**Streamlit Cloud** se actualizará automáticamente al detectar cambios en GitHub.

---

## 📝 Archivos Principales a Subir

Asegúrate de que estos archivos estén en el repo:

- ✅ `app_extractor_v3.py` - Aplicación principal
- ✅ `requirements_app.txt` - Dependencias Python
- ✅ `packages.txt` - Dependencias del sistema
- ✅ `README.md` - Documentación
- ✅ `LICENSE` - Licencia del proyecto
- ✅ `.gitignore` - Archivos a ignorar
- ✅ `.streamlit/config.toml` - Configuración
- ✅ `EJECUTAR_APP.bat` - Script de inicio

**NO** subas:
- ❌ Archivos de prueba (`test_*.py`, `*_backup.py`)
- ❌ PDFs o imágenes de ejemplo
- ❌ Entornos virtuales (`venv/`, `.venv/`)
- ❌ Archivos personales o bases de datos

---

## 🆘 Solución de Problemas

### Error: "remote origin already exists"
```powershell
git remote remove origin
git remote add origin https://github.com/TU_USUARIO/extractor-documentos.git
```

### Error de autenticación
- Usa un [Personal Access Token](https://github.com/settings/tokens/new)
- Scope necesario: `repo`
- Úsalo como contraseña cuando Git lo pida

### No puedo hacer push
```powershell
git pull origin main --allow-unrelated-histories
git push -u origin main
```

---

## ✅ Checklist Final

Antes de publicar, verifica:

- [ ] README.md está actualizado con tu nombre de usuario
- [ ] LICENSE tiene la información correcta
- [ ] .gitignore excluye archivos sensibles
- [ ] requirements_app.txt tiene todas las dependencias
- [ ] La app funciona localmente
- [ ] No hay credenciales o datos sensibles en el código

---

## 📧 Necesitas Ayuda?

- [Documentación de Git](https://git-scm.com/doc)
- [GitHub Docs](https://docs.github.com/)
- [Streamlit Cloud Docs](https://docs.streamlit.io/streamlit-community-cloud)

¡Éxitos con tu proyecto! 🚀
