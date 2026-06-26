@echo off
echo ============================================
echo   Servidor local - Residencia Ildefonso
echo ============================================
echo.
echo Iniciando servidor en http://localhost:8080
echo Para detenerlo, cierra esta ventana o pulsa Ctrl+C
echo.

REM Intenta con Python 3
python -m http.server 8080 --directory "%~dp0" 2>nul
if %errorlevel% neq 0 (
    REM Intenta con Python (sin version)
    python3 -m http.server 8080 --directory "%~dp0" 2>nul
    if %errorlevel% neq 0 (
        echo ERROR: No se encontro Python instalado.
        echo Instala Python desde https://www.python.org/downloads/
        echo o usa Node.js con: npx serve .
        pause
    )
)
