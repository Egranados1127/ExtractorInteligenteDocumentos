@echo off
echo ========================================
echo   EXTRACTOR DE RESOLUCIONES - APP WEB
echo ========================================
echo.

REM Verificar si existe el entorno virtual
if not exist "venv_app\Scripts\activate.bat" (
    echo [1/3] Creando entorno virtual...
    python -m venv venv_app
    if errorlevel 1 (
        echo ERROR: No se pudo crear el entorno virtual
        echo Verifica que Python este instalado
        pause
        exit /b 1
    )
)

echo [2/3] Activando entorno virtual...
call venv_app\Scripts\activate.bat

echo [3/3] Instalando dependencias...
pip install -r requirements_app.txt --quiet

echo.
echo ========================================
echo   INICIANDO APLICACION...
echo ========================================
echo.
echo La aplicacion se abrira automaticamente en tu navegador.
echo Si no se abre, visita: http://localhost:8501
echo.
echo Para detener la aplicacion, presiona Ctrl+C
echo.

streamlit run app_extractor.py

pause
