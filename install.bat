@echo off
echo ========================================
echo Instalador Markdown Viewer
echo ========================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no está instalado o no está en PATH
    echo Descarga Python desde: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [1/4] Creando entorno virtual...
python -m venv venv
if errorlevel 1 (
    echo ERROR: No se pudo crear el entorno virtual
    pause
    exit /b 1
)

echo [2/4] Activando entorno virtual...
call venv\Scripts\activate.bat

echo [3/4] Instalando dependencias...
pip install --upgrade pip
pip install -r requirements.txt

echo [4/4] Descargando wkhtmltopdf para exportación PDF...
echo.
echo IMPORTANTE: Para exportar a PDF necesitas instalar wkhtmltopdf
echo Descarga desde: https://wkhtmltopdf.org/downloads.html
echo.

echo ========================================
echo Instalación completada!
echo ========================================
echo.
echo Para ejecutar la aplicación:
echo   1. Doble clic en run.bat
echo   O desde consola:
echo   2. venv\Scripts\activate
echo   3. python MarkdownViewer.py
echo.
pause
