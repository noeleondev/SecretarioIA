#!/bin/bash
# ============================================
#  SCRIPT DE INICIO - SECRETARIO IA V3
# ============================================

echo ""
echo "=========================================="
echo "   🤖 SECRETARIO IA V3"
echo "=========================================="
echo ""

# 1. Ir a la carpeta del script
cd "$(dirname "$0")"

# 2. Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python no está instalado."
    exit 1
fi

# 3. Verificar entorno virtual
if [ ! -d "venv" ]; then
    echo "[INFO] Creando entorno virtual..."
    python3 -m venv venv
fi

# 4. Activar entorno virtual
echo "[INFO] Activando entorno virtual..."
source venv/bin/activate

# 5. Instalar dependencias
if ! python -c "import telegram" &> /dev/null; then
    echo "[INFO] Instalando dependencias..."
    pip install -r requirements.txt
fi

# 6. Iniciar el bot
echo ""
echo "[INFO] Iniciando el bot..."
echo ""
python src/main.py