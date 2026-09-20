@echo off
REM ============================================
REM  CONFIGURACIÓN INICIAL - SECRETARIO IA V3
REM ============================================
REM  Este script:
REM  1. Crea el entorno virtual
REM  2. Instala las dependencias
REM  3. Crea el archivo .env desde .env.example
REM ============================================

echo.
echo ==========================================
echo   CONFIGURACION INICIAL
echo ==========================================
echo.

cd /d "%~dp0"

REM 1. Crear entorno virtual
echo [1/3] Creando entorno virtual...
python -m venv venv
if errorlevel 1 (
    echo [ERROR] No se pudo crear el entorno virtual.
    pause
    exit /b 1
)

REM 2. Activar e instalar dependencias
echo [2/3] Instalando dependencias...
call venv\Scripts\activate
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] No se pudieron instalar las dependencias.
    pause
    exit /b 1
)

REM 3. Crear .env desde .env.example
echo [3/3] Creando archivo .env...
if not exist .env (
    copy .env.example .env
    echo [OK] Archivo .env creado desde .env.example
    echo [WARN] IMPORTANTE: Edita el .env con tus valores.
) else (
    echo [OK] El archivo .env ya existe.
)

echo.
echo [OK] Configuracion completa.
echo Ahora puedes ejecutar run.bat para iniciar el bot.
pause