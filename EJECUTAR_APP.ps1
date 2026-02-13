# ========================================
# SISTEMA INTEGRADO DE EXTRACCION
# ========================================

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  SISTEMA INTEGRADO DE EXTRACCION" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

Write-Host "Nuevo Sistema con 6 Estrategias:" -ForegroundColor Green
Write-Host "  - AUTO (Recomendado): Seleccion inteligente" -ForegroundColor White
Write-Host "  - RAPIDO: Tesseract (1-2 seg)" -ForegroundColor White
Write-Host "  - BALANCEADO: Tesseract + PaddleOCR (3-5 seg)" -ForegroundColor White
Write-Host "  - PRECISO: EasyOCR + PaddleOCR (10-15 seg)" -ForegroundColor White
Write-Host "  - AZURE: Document Intelligence (2-4 seg)" -ForegroundColor White
Write-Host "  - COMPARAR: Todos los metodos`n" -ForegroundColor White

Write-Host "URL: http://localhost:8501" -ForegroundColor Cyan
Write-Host "Presiona Ctrl+C para detener`n" -ForegroundColor Yellow

streamlit run app_maestro.py
