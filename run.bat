@echo off
REM ============================================
REM  SCRIPT DE INICIO - SECRETARIO IA V3
REM ============================================
REM  Este script:
REM  1. Activa el entorno virtual
REM  2. Instala las dependencias (si faltan)
REM  3. Inicia el bot
REM ============================================

echo.
echo ==========================================
echo   🤖 SECRETARIO IA V3
echo ==========================================
echo.

REM 1. Cambiar a la carpeta del script
cd /d "%~dp0"

REM 2. Verificar que Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no está instalado o no está en el PATH.
    echo Por favor, instala Python 3.11.9 y marca "Add to PATH".
    pause
    exit /b 1
)

REM 3. Verificar que existe el entorno virtual
if not exist venv\Scripts\activate (
    echo [INFO] No existe el entorno virtual. Creándolo...
    python -m venv venv
    if errorlevel 1 (
        echo [ERROR] No se pudo crear el entorno virtual.
        pause
        exit /b 1
    )
    echo [OK] Entorno virtual creado.
)

REM 4. Activar el entorno virtual
echo [INFO] Activando entorno virtual...
call venv\Scripts\activate

REM 5. Instalar dependencias si faltan
echo [INFO] Verificando dependencias...
python -c "import telegram" >nul 2>&1
if errorlevel 1 (
    echo [INFO] Instalando dependencias...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [ERROR] No se pudieron instalar las dependencias.
        pause
        exit /b 1
    )
    echo [OK] Dependencias instaladas.
)

REM 6. Iniciar el bot
echo.
echo [INFO] Iniciando el bot...
echo.
python src\main.py

REM 7. Pausa al terminar (para ver errores)
echo.
echo [INFO] El bot se ha detenido.
pause