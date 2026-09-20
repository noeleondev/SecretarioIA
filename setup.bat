@echo off
REM ============================================
REM  CONFIGURACIÓN INICIAL - SECRETARIO IA V3
REM ============================================
REM  Este script hace TODO automáticamente:
REM  1. Crea el entorno virtual
REM  2. Instala las dependencias
REM  3. Crea el archivo .env desde .env.example
REM  4. Abre el .env para que pongas tu token
REM  5. Crea la carpeta Almacenamiento/vault si no existe
REM ============================================

echo.
echo ==========================================
echo   CONFIGURACION INICIAL - SECRETARIO IA V3
echo ==========================================
echo.

cd /d "%~dp0"

REM 1. Verificar Python
echo [1/5] Verificando Python...
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

REM 2. Crear entorno virtual
echo [2/5] Creando entorno virtual...
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

REM 3. Instalar dependencias
echo [3/5] Instalando dependencias...
call venv\Scripts\activate
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] No se pudieron instalar las dependencias.
    pause
    exit /b 1
)
echo [OK] Dependencias instaladas.

REM 4. Crear .env desde .env.example
echo [4/5] Configurando variables de entorno...
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

REM 5. Crear carpeta Almacenamiento/vault si no existe
echo [5/5] Verificando carpeta de Almacenamiento...
if not exist "..\Almacenamiento\vault" (
    mkdir "..\Almacenamiento\vault"
    echo [OK] Carpeta Almacenamiento\vault creada.
) else (
    echo [OK] Carpeta Almacenamiento\vault ya existe.
)

echo.
echo ==========================================
echo   CONFIGURACION COMPLETA
echo ==========================================
echo.
echo Ahora puedes ejecutar: run.bat
echo.
pause