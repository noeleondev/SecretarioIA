# src/utils/validators.py
"""
Módulo de validaciones.

Contiene funciones para validar entradas del usuario, como fechas,
puntajes, nombres de archivo, etc.
"""

import re
from datetime import datetime
from typing import Optional, Tuple


class Validator:
    """
    Clase con métodos estáticos para validar datos.
    """

    @staticmethod
    def validate_date(date_str: str, date_format: str = "%Y-%m-%d") -> bool:
        """
        Valida que una fecha tenga el formato correcto.

        Args:
            date_str: Fecha a validar.
            date_format: Formato esperado.

        Returns:
            True si es válida, False en caso contrario.
        """
        try:
            datetime.strptime(date_str, date_format)
            return True
        except (ValueError, TypeError):
            return False

    @staticmethod
    def validate_mood_score(score: int) -> bool:
        """
        Valida que un puntaje esté en el rango 1-10.

        Args:
            score: Puntaje a validar.

        Returns:
            True si está en el rango, False en caso contrario.
        """
        try:
            return 1 <= int(score) <= 10
        except (ValueError, TypeError):
            return False

    @staticmethod
    def sanitize_filename(filename: str) -> str:
        """
        Limpia un nombre de archivo eliminando caracteres no permitidos.

        Args:
            filename: Nombre original.

        Returns:
            Nombre sanitizado.
        """
        # Eliminar caracteres no permitidos en Windows
        filename = re.sub(r'[<>:"/\\|?*]', "", filename)
        # Eliminar espacios al inicio y final
        filename = filename.strip()
        # Limitar longitud
        return filename[:100]

    @staticmethod
    def parse_mood_input(text: str) -> Tuple[Optional[int], Optional[str]]:
        """
        Parsea el estado de ánimo de un texto.

        Ejemplos:
            "8" → (8, None)
            "8 estoy bien" → (8, "estoy bien")

        Args:
            text: Texto a parsear.

        Returns:
            Tupla (puntaje, comentario) o (None, None) si falla.
        """
        parts = text.strip().split(maxsplit=1)

        try:
            score = int(parts[0])
            if not Validator.validate_mood_score(score):
                return None, None
            comment = parts[1] if len(parts) > 1 else None
            return score, comment
        except (ValueError, IndexError):
            return None, None