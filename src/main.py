# src/main.py
"""
Punto de entrada del Secretario IA V3.

Uso:
    python src/main.py
"""

import sys
from pathlib import Path

# Agregar el directorio raíz al PATH para importar módulos
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.core.config import Config
from src.core.logger import setup_logger
from src.core.bot import SecretarioBot


def main():
    """Función principal."""
    print("=" * 50)
    print("🤖 SECRETARIO IA V3")
    print("=" * 50)

    try:
        # 1. Cargar configuración
        config = Config()
        print("✅ Configuración cargada")

        # 2. Configurar logs
        setup_logger(config)
        print("✅ Sistema de logs iniciado")

        # 3. Iniciar bot
        bot = SecretarioBot(config)
        print("✅ Bot iniciado")
        print("=" * 50)
        print("Presiona Ctrl+C para detener")
        print("=" * 50)

        bot.run()

    except KeyboardInterrupt:
        print("\n👋 Bot detenido por el usuario")
    except Exception as e:
        print(f"❌ Error fatal: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()