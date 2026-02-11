# ========================================
# EXTRACTOR DE RESOLUCIONES - APP WEB
# ========================================

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  EXTRACTOR DE RESOLUCIONES - APP WEB" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar si existe el entorno virtual
if (-not (Test-Path "venv_app\Scripts\Activate.ps1")) {
    Write-Host "[1/3] Creando entorno virtual..." -ForegroundColor Yellow
    python -m venv venv_app
    if ($LASTEXITCODE -ne 0) {
        Write-Host "ERROR: No se pudo crear el entorno virtual" -ForegroundColor Red
        Write-Host "Verifica que Python este instalado" -ForegroundColor Red
        Read-Host "Presiona Enter para salir"
        exit 1
    }
}

Write-Host "[2/3] Activando entorno virtual..." -ForegroundColor Yellow
& "venv_app\Scripts\Activate.ps1"

Write-Host "[3/3] Instalando dependencias..." -ForegroundColor Yellow
pip install -r requirements_app.txt --quiet

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "  INICIANDO APLICACION..." -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "La aplicacion se abrira automaticamente en tu navegador." -ForegroundColor White
Write-Host "Si no se abre, visita: http://localhost:8501" -ForegroundColor White
Write-Host ""
Write-Host "Para detener la aplicacion, presiona Ctrl+C" -ForegroundColor Yellow
Write-Host ""

streamlit run app_extractor.py
