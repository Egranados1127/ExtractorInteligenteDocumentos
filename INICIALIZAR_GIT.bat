@echo off
echo ============================================
echo Inicializando Repositorio Git
echo ============================================
echo.

cd /d "%~dp0"

echo [1/5] Inicializando Git...
git init
if errorlevel 1 (
    echo ERROR: Git no esta instalado. Descargalo de https://git-scm.com/downloads
    pause
    exit /b 1
)

echo.
echo [2/5] Agregando archivos al repositorio...
git add .

echo.
echo [3/5] Creando primer commit...
git commit -m "Primera version: Extractor Inteligente de Documentos"

echo.
echo [4/5] Configuracion completada
echo.
echo ============================================
echo PROXIMOS PASOS:
echo ============================================
echo.
echo 1. Ve a https://github.com/new
echo 2. Crea un nuevo repositorio (puedes llamarlo "extractor-documentos")
echo 3. NO marques "Add a README file"
echo 4. Copia el repositorio URL (ejemplo: https://github.com/usuario/extractor-documentos.git)
echo 5. Vuelve aqui y ejecuta estos comandos:
echo.
echo    git remote add origin https://github.com/TU_USUARIO/extractor-documentos.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo ============================================
echo.
pause
