# src/core/logger.py
"""
Módulo de logging.

Configura el sistema de logs con rotación de archivos y salida
a consola. Todos los módulos deben usar `get_logger(__name__)`.
"""

import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

from src.core.config import Config


def setup_logger(config: Config) -> logging.Logger:
    """
    Configura el sistema de logs.

    Args:
        config: Objeto de configuración.

    Returns:
        El logger raíz configurado.
    """
    # Crear carpeta de logs si no existe
    log_dir = Path(config.get("paths.logs", "./logs"))
    log_dir.mkdir(parents=True, exist_ok=True)

    # Nombre del archivo de log con fecha
    log_file = log_dir / "secretario.log"

    # Formato de los logs
    format_str = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(format_str, date_format)

    # Logger raíz
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # Evitar duplicar handlers si se llama varias veces
    if root_logger.handlers:
        root_logger.handlers.clear()

    # Handler para archivo con rotación (10 MB, 5 backups)
    file_handler = RotatingFileHandler(
        log_file, maxBytes=10 * 1024 * 1024, backupCount=5, encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)

    # Handler para consola
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    return root_logger


def get_logger(name: str) -> logging.Logger:
    """
    Obtiene un logger con el nombre especificado.

    Args:
        name: Nombre del logger (usar `__name__`).

    Returns:
        Instancia del logger.
    """
    return logging.getLogger(name)