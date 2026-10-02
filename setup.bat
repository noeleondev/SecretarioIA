@echo off
REM ============================================
REM  CONFIGURACIÓN INICIAL - SECRETARIO IA V3
REM ============================================
REM  Este script hace TODO automáticamente:
REM  1. Verifica Python
REM  2. Crea el entorno virtual
REM  3. Actualiza pip, setuptools y wheel
REM  4. Instala las dependencias básicas
REM  5. Instala las dependencias de voz (opcional)
REM  6. Crea el archivo .env desde .env.example
REM  7. Abre el .env para que pongas tu token
REM  8. Crea la carpeta Almacenamiento/vault si no existe
REM ============================================

echo.
echo ==========================================
echo   CONFIGURACION INICIAL - SECRETARIO IA V3
echo ==========================================
echo.

cd /d "%~dp0"

REM ============================================
REM PASO 1: Verificar Python
REM ============================================
echo [1/8] Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no esta instalado.
    echo.
    echo Descargalo desde: https://www.python.org/downloads/release/python-3119/
    echo IMPORTANTE: Marca "Add python.exe to PATH" durante la instalacion.
    pause
    exit /b 1
)
echo [OK] Python encontrado.

REM ============================================
REM PASO 2: Crear entorno virtual
REM ============================================
echo [2/8] Creando entorno virtual...
if exist venv (
    echo [OK] El entorno virtual ya existe.
) else (
    python -m venv venv
    if errorlevel 1 (
        echo [ERROR] No se pudo crear el entorno virtual.
        pause
        exit /b 1
    )
    echo [OK] Entorno virtual creado.
)

REM ============================================
REM PASO 3: Activar entorno virtual
REM ============================================
call venv\Scripts\activate

REM ============================================
REM PASO 4: Actualizar pip, setuptools y wheel
REM ============================================
echo [3/8] Actualizando pip, setuptools y wheel...
python -m pip install --upgrade pip setuptools wheel
if errorlevel 1 (
    echo [WARN] No se pudieron actualizar pip/setuptools/wheel.
) else (
    echo [OK] pip, setuptools y wheel actualizados.
)

REM ============================================
REM PASO 5: Instalar dependencias basicas
REM ============================================
echo [4/8] Instalando dependencias basicas...
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] No se pudieron instalar las dependencias basicas.
    pause
    exit /b 1
)
echo [OK] Dependencias basicas instaladas.

REM ============================================
REM PASO 6: Instalar dependencias de voz (opcional)
REM ============================================
echo [5/8] Instalando dependencias de voz (opcional)...
echo [INFO] Instalando sounddevice y soundfile...
pip install sounddevice==0.4.6 soundfile==0.12.1 >nul 2>&1
if errorlevel 1 (
    echo [WARN] No se pudieron instalar sounddevice/soundfile.
) else (
    echo [OK] sounddevice y soundfile instalados.
)

echo [INFO] Instalando openai-whisper desde GitHub...
pip install git+https://github.com/openai/whisper.git >nul 2>&1
if errorlevel 1 (
    echo [WARN] No se pudo instalar openai-whisper.
    echo [WARN] El bot funcionara sin mensajes de voz.
    echo [WARN] Si quieres usar voz, instala manualmente:
    echo [WARN]   pip install git+https://github.com/openai/whisper.git
) else (
    echo [OK] openai-whisper instalado.
)

REM ============================================
REM PASO 7: Crear .env desde .env.example
REM ============================================
echo [6/8] Configurando variables de entorno...
if exist .env (
    echo [OK] El archivo .env ya existe.
) else (
    copy .env.example .env >nul
    echo [OK] Archivo .env creado desde .env.example.
    echo.
    echo ==========================================
    echo   IMPORTANTE: CONFIGURA TU TOKEN
    echo ==========================================
    echo.
    echo Se abrira el archivo .env en el Bloc de notas.
    echo Por favor, reemplaza:
    echo     AQUI_VA_TU_TOKEN_DE_TELEGRAM
    echo por tu token real de Telegram.
    echo.
    echo Si no tienes un token, habla con @BotFather en Telegram.
    echo.
    pause
    notepad .env
)

REM ============================================
REM PASO 8: Crear carpeta Almacenamiento/vault
REM ============================================
echo [7/8] Verificando carpeta de Almacenamiento...
if not exist "..\Almacenamiento\vault" (
    mkdir "..\Almacenamiento\vault"
    echo [OK] Carpeta Almacenamiento\vault creada.
) else (
    echo [OK] Carpeta Almacenamiento\vault ya existe.
)

REM ============================================
REM PASO 9: Verificar instalacion
REM ============================================
echo [8/8] Verificando instalacion...
python -c "import telegram; print('  [OK] python-telegram-bot')" 2>nul
if errorlevel 1 (
    echo   [ERROR] python-telegram-bot no esta instalado.
) else (
    echo   [OK] python-telegram-bot
)

python -c "import yaml; print('  [OK] pyyaml')" 2>nul
if errorlevel 1 (
    echo   [ERROR] pyyaml no esta instalado.
) else (
    echo   [OK] pyyaml
)

python -c "import dotenv; print('  [OK] python-dotenv')" 2>nul
if errorlevel 1 (
    echo   [ERROR] python-dotenv no esta instalado.
) else (
    echo   [OK] python-dotenv
)

python -c "import requests; print('  [OK] requests')" 2>nul
if errorlevel 1 (
    echo   [ERROR] requests no esta instalado.
) else (
    echo   [OK] requests
)

python -c "import whisper; print('  [OK] openai-whisper')" 2>nul
if errorlevel 1 (
    echo   [WARN] openai-whisper no esta instalado (voz deshabilitada)
) else (
    echo   [OK] openai-whisper
)

REM ============================================
REM FINALIZAR
REM ============================================
echo.
echo ==========================================
echo   CONFIGURACION COMPLETA
echo ==========================================
echo.
echo Ahora puedes ejecutar: run.bat
echo.
pause