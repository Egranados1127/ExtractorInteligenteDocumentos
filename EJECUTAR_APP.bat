@echo off
echo.
echo ========================================================
echo    SISTEMA INTEGRADO DE EXTRACCION DE DOCUMENTOS
echo ========================================================
echo.
echo Nuevo: 6 Estrategias de Extraccion
echo   - AUTO (Recomendado): Seleccion inteligente
echo   - RAPIDO: Tesseract (1-2s)
echo   - BALANCEADO: Tesseract + PaddleOCR (3-5s)
echo   - PRECISO: EasyOCR + PaddleOCR (10-15s)
echo   - AZURE: Document Intelligence (2-4s)
echo   - COMPARAR: Todos los metodos
echo.
echo URL: http://localhost:8501
echo Presiona Ctrl+C para detener
echo.

streamlit run app_maestro.py

pause
