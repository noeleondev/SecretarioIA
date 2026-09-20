# src/modules/llm.py
"""
Módulo de comunicación con LM Studio.

Envía mensajes al modelo de IA local y procesa las respuestas.
"""

import json
import re
import time
import logging
import requests
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


class LLMClient:
    """
    Cliente para comunicarse con LM Studio.

    Ejemplo:
        llm = LLMClient(config)
        respuesta = llm.interpretar("Agenda tarea para el jueves")
    """

    def __init__(self, config: dict):
        """
        Inicializa el cliente.

        Args:
            config: Configuración con URL, modelo, timeout, etc.
        """
        self.url = config.get("url", "http://localhost:1234/v1/chat/completions")
        self.model = config.get("model", "Qwen3-4B-2507")
        self.timeout = config.get("timeout", 120)
        self.max_retries = config.get("max_retries", 3)

    def _post(self, prompt: str, max_tokens: int = 500) -> Optional[str]:
        """
        Envía una petición POST a LM Studio.

        Args:
            prompt: Texto del prompt.
            max_tokens: Número máximo de tokens a generar.

        Returns:
            Contenido de la respuesta o None si falla.
        """
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": "Responde SOLO con JSON válido. NUNCA uses markdown.",
                },
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.0,
            "max_tokens": max_tokens,
        }

        for intento in range(self.max_retries):
            try:
                response = requests.post(
                    self.url, json=payload, timeout=self.timeout
                )
                response.raise_for_status()
                return response.json()["choices"][0]["message"]["content"]

            except requests.exceptions.ConnectionError:
                logger.error("❌ No se pudo conectar a LM Studio")
                return None
            except requests.exceptions.Timeout:
                logger.warning(
                    f"⏳ Timeout (intento {intento + 1}/{self.max_retries})"
                )
                time.sleep(2)
            except Exception as e:
                logger.error(f"❌ Error: {e}")
                if intento < self.max_retries - 1:
                    time.sleep(2)
                else:
                    return None

        return None

    def _extract_json(self, text: str) -> Optional[Dict[str, Any]]:
        """
        Extrae un JSON válido de un texto.

        Args:
            text: Texto que puede contener JSON.

        Returns:
            Diccionario parseado o None si falla.
        """
        if not text:
            return None

        # Limpiar markdown
        text = text.strip()
        if text.startswith("```"):
            lines = text.split("\n")
            text = "\n".join(lines[1:-1]) if len(lines) > 2 else text
            text = text.replace("```json", "").replace("```", "").strip()

        # Buscar JSON con regex
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                pass

        return None

    def interpretar(self, mensaje: str) -> Dict[str, Any]:
        """
        Interpreta un mensaje del usuario.

        Args:
            mensaje: Mensaje del usuario.

        Returns:
            Diccionario con la acción detectada.
        """
        prompt = self._build_prompt(mensaje)
        response = self._post(prompt)

        if response:
            data = self._extract_json(response)
            if data:
                logger.info(f"✅ Comando interpretado: {data}")
                return data

        logger.warning("⚠️ No se pudo interpretar el mensaje")
        return {"accion": "desconocido"}

    def _build_prompt(self, mensaje: str) -> str:
        """
        Construye el prompt para el modelo.

        Args:
            mensaje: Mensaje del usuario.

        Returns:
            Prompt completo.
        """
        return f"""
Eres un asistente de agenda. Responde SOLO con JSON.

ACCIONES:
- Agendar: {{"accion": "agendar", "tarea": "...", "materia": "...", "fecha": "..."}}
- Consultar: {{"accion": "consultar", "filtro": "hoy|semana|todas"}}
- Completar: {{"accion": "completar", "tarea": "..."}}
- Eliminar: {{"accion": "eliminar", "tarea": "..."}}

FECHAS: "jueves", "16", "jueves 16", "hoy", "mañana".

Usuario: "{mensaje}"

RESPUESTA (SOLO JSON):
"""