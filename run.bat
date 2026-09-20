@echo off
REM ============================================
REM  INICIO DEL BOT - SECRETARIO IA V3
REM ============================================
REM  Este script:
REM  1. Activa el entorno virtual
REM  2. Inicia el bot
REM ============================================

echo.
echo ==========================================
echo   SECRETARIO IA V3
echo ==========================================
echo.

cd /d "%~dp0"

REM 1. Verificar que existe el entorno virtual
if not exist venv\Scripts\activate (
    echo [ERROR] No existe el entorno virtual.
    echo Por favor, ejecuta primero: setup.bat
    pause
    exit /b 1
)

REM 2. Activar entorno virtual
call venv\Scripts\activate

REM 3. Verificar que existe el .env
if not exist .env (
    echo [ERROR] No existe el archivo .env.
    echo Por favor, ejecuta primero: setup.bat
    pause
    exit /b 1
)

REM 4. Verificar LM Studio
echo [INFO] Verificando LM Studio...
curl -s http://localhost:1234/v1/models >nul 2>&1
if errorlevel 1 (
    echo.
    echo [WARN] LM Studio no responde en http://localhost:1234
    echo.
    echo Asegurate de que:
    echo   1. LM Studio esta abierto
    echo   2. El modelo Qwen3-4B-2507 esta cargado
    echo   3. El servidor esta activo (pestana "Server")
    echo.
    choice /C SN /M "Continuar de todas formas"
    if errorlevel 2 exit /b 1
)

REM 5. Iniciar el bot
echo.
echo [INFO] Iniciando el bot...
echo.
python src\main.py

REM 6. Pausa al terminar
echo.
echo [INFO] El bot se ha detenido.
pause