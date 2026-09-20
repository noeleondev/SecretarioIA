# src/core/config.py
"""
Módulo de configuración.

Carga la configuración del archivo `config/config.yaml` y las
variables de entorno del archivo `.env`. Proporciona una interfaz
única para acceder a todos los valores de configuración.
"""

import os
from pathlib import Path
from typing import Any, Dict

import yaml
from dotenv import load_dotenv


class Config:
    """
    Clase que gestiona la configuración del bot.

    Carga los valores desde `config/config.yaml` y las variables
    de entorno desde el archivo `.env`.

    Ejemplo de uso:
        config = Config()
        modelo = config.get("llm.model")  # Retorna "Qwen3-4B-2507"
    """

    def __init__(self, config_path: str = "config/config.yaml"):
        """
        Inicializa la configuración.

        Args:
            config_path: Ruta al archivo `config.yaml`.
        """
        # 1. Cargar variables de entorno (.env)
        load_dotenv()

        # 2. Cargar archivo YAML
        self.config_path = Path(config_path)
        if not self.config_path.exists():
            raise FileNotFoundError(
                f"No se encontró el archivo de configuración: {config_path}"
            )

        with open(self.config_path, "r", encoding="utf-8") as f:
            self._config = yaml.safe_load(f)

        # 3. Inyectar variables de entorno en la configuración
        self._inject_env_variables()

    def _inject_env_variables(self):
        """
        Reemplaza los placeholders de variables de entorno en la
        configuración por sus valores reales.
        """
        # Token de Telegram (obligatorio)
        telegram_token = os.getenv("TELEGRAM_TOKEN")
        if telegram_token:
            self._config.setdefault("telegram", {})
            self._config["telegram"]["token"] = telegram_token

        # Ruta del Vault de Obsidian
        vault_path = os.getenv("VAULT_PATH")
        if vault_path:
            self._config["paths"]["vault"] = vault_path

        # Ruta de FFmpeg
        ffmpeg_path = os.getenv("FFMPEG_PATH")
        if ffmpeg_path:
            self._config["paths"]["ffmpeg"] = ffmpeg_path

        # URL de LM Studio
        lm_url = os.getenv("LM_STUDIO_URL")
        if lm_url:
            self._config["llm"]["url"] = lm_url

        # Modelo de LM Studio
        lm_model = os.getenv("LM_STUDIO_MODEL")
        if lm_model:
            self._config["llm"]["model"] = lm_model

    def get(self, key: str, default: Any = None) -> Any:
        """
        Obtiene un valor de la configuración usando notación de puntos.

        Args:
            key: Ruta de la clave (ej: "llm.model").
            default: Valor por defecto si no se encuentra la clave.

        Returns:
            El valor de la configuración o el valor por defecto.

        Ejemplo:
            config.get("llm.model")       # "Qwen3-4B-2507"
            config.get("paths.vault")      # "./data/vault"
            config.get("no.existe", 42)    # 42
        """
        keys = key.split(".")
        value = self._config

        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default

        return value

    def get_all(self) -> Dict[str, Any]:
        """
        Retorna toda la configuración como un diccionario.

        Returns:
            Diccionario con toda la configuración.
        """
        return self._config

    def reload(self):
        """
        Recarga la configuración desde el archivo.
        Útil si el archivo se modificó en tiempo de ejecución.
        """
        with open(self.config_path, "r", encoding="utf-8") as f:
            self._config = yaml.safe_load(f)
        self._inject_env_variables()