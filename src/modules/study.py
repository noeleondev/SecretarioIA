# src/modules/study.py
"""
Módulo del sistema de estudio.

Divide temas en pasos y gestiona las sesiones de estudio.
"""

import logging
from pathlib import Path
from typing import Dict, List

logger = logging.getLogger(__name__)


class StudyManager:
    """
    Gestor del sistema de estudio.

    Ejemplo:
        study = StudyManager(config)
        sesion = study.iniciar_sesion("Ingles", "El_alfabeto")
    """

    def __init__(self, config: dict):
        """Inicializa el gestor."""
        self.config = config
        self.base_path = Path(config.get("paths", {}).get("vault", "./data/vault")) / "estudios"

    def iniciar_sesion(self, materia: str, tema: str) -> Dict:
        """
        Inicia una sesión de estudio.

        Args:
            materia: Nombre de la materia.
            tema: Nombre del tema.

        Returns:
            Diccionario con el resultado.
        """
        ruta = self.base_path / materia / tema

        if not ruta.exists():
            return {
                "success": False,
                "message": f"❌ No encontré el tema '{tema}' en '{materia}'",
            }

        contenido = (ruta / "contenido.md").read_text(encoding="utf-8")

        pasos = [
            {"paso": 1, "descripcion": f"📖 Lee: {tema}", "tiempo": 5},
            {"paso": 2, "descripcion": "✍️ Practica con ejemplos", "tiempo": 5},
            {"paso": 3, "descripcion": "🔁 Repasa lo aprendido", "tiempo": 5},
        ]

        return {
            "success": True,
            "materia": materia,
            "tema": tema,
            "contenido": contenido,
            "pasos": pasos,
        }

    def listar_temas(self, materia: str) -> List[str]:
        """
        Lista los temas disponibles de una materia.

        Args:
            materia: Nombre de la materia.

        Returns:
            Lista de nombres de temas.
        """
        ruta = self.base_path / materia
        if not ruta.exists():
            return []
        return [d.name for d in ruta.iterdir() if d.is_dir()]