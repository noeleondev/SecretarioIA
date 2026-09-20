# src/utils/date_parser.py
"""
Módulo de parseo de fechas.

Convierte expresiones de fecha en lenguaje natural (ej. "jueves",
"16", "mañana", "hoy") al formato estándar `YYYY-MM-DD`.

Ejemplo:
    parser = DateParser({"weekdays": {...}, ...})
    fecha = parser.parse("jueves")  # "2026-09-24"
"""

import re
import logging
from datetime import datetime, timedelta
from typing import Optional

logger = logging.getLogger(__name__)


class DateParser:
    """
    Parsea fechas en lenguaje natural al formato YYYY-MM-DD.

    Soporta:
        - "hoy", "mañana", "pasado mañana"
        - "jueves", "lunes", etc. (próximo día de la semana)
        - "16" (día 16 del mes actual)
        - "jueves 16" (jueves 16 del mes actual)
        - "2026-09-20" (formato específico)
    """

    def __init__(self, config: dict):
        """
        Inicializa el parser con la configuración.

        Args:
            config: Diccionario con la configuración del parser.
                Debe incluir:
                - weekdays: Mapa de nombres de días a números (0=lunes)
                - date_keywords: Mapa de palabras clave a días de diferencia
                - date_format: Formato de fecha (por defecto: "%Y-%m-%d")
        """
        self.weekdays = config.get("weekdays", {})
        self.date_keywords = config.get("date_keywords", {})
        self.date_format = config.get("date_format", "%Y-%m-%d")

    def parse(self, text: str) -> Optional[str]:
        """
        Parsea un texto a una fecha en formato YYYY-MM-DD.

        Args:
            text: Texto a parsear (ej. "jueves", "16", "mañana").

        Returns:
            Fecha en formato YYYY-MM-DD o None si no se puede parsear.
        """
        if not text:
            return None

        text = text.lower().strip()

        # ============================================
        # CASO 1: Palabras clave (hoy, mañana, etc.)
        # ============================================
        if text in self.date_keywords:
            days = self.date_keywords[text]
            return (datetime.now() + timedelta(days=days)).strftime(self.date_format)

        # ============================================
        # CASO 2: Día de la semana + número (jueves 16)
        # ============================================
        weekday_pattern = (
            r"(lunes|martes|miércoles|miercoles|jueves|viernes|sábado|sabado|domingo)"
            r"\s*(\d{1,2})?"
        )
        match = re.search(weekday_pattern, text)
        if match:
            weekday_name = match.group(1)
            day_number = match.group(2)

            # Normalizar el nombre del día
            weekday_name = self._normalize_weekday(weekday_name)
            target_weekday = self.weekdays.get(weekday_name)

            if target_weekday is not None:
                today = datetime.now()
                days_ahead = target_weekday - today.weekday()
                if days_ahead <= 0:
                    days_ahead += 7

                target_date = today + timedelta(days=days_ahead)

                # Si se especificó un número de día, intentar ajustar
                if day_number:
                    day_number = int(day_number)
                    try:
                        target_date = target_date.replace(day=day_number)
                    except ValueError:
                        # El día no existe en ese mes, ir al siguiente
                        if day_number > 28:
                            next_month = target_date.month + 1
                            if next_month > 12:
                                next_month = 1
                                target_date = target_date.replace(
                                    year=target_date.year + 1
                                )
                            target_date = target_date.replace(
                                month=next_month, day=day_number
                            )

                return target_date.strftime(self.date_format)

        # ============================================
        # CASO 3: Solo número (16)
        # ============================================
        day_match = re.match(r"^(\d{1,2})$", text)
        if day_match:
            day = int(day_match.group(1))
            today = datetime.now()
            try:
                date_obj = today.replace(day=day)
                if date_obj < today:
                    # Si ya pasó, ir al siguiente mes
                    if today.month == 12:
                        date_obj = today.replace(
                            year=today.year + 1, month=1, day=day
                        )
                    else:
                        date_obj = today.replace(month=today.month + 1, day=day)
                return date_obj.strftime(self.date_format)
            except ValueError:
                return None

        # ============================================
        # CASO 4: Formato específico (2026-09-20)
        # ============================================
        try:
            datetime.strptime(text, self.date_format)
            return text
        except ValueError:
            pass

        # ============================================
        # CASO 5: No se pudo parsear
        # ============================================
        logger.warning(f"No se pudo parsear la fecha: {text}")
        return None

    def _normalize_weekday(self, name: str) -> str:
        """
        Normaliza el nombre del día de la semana.

        Corrige errores comunes: "miercoles" → "miércoles".

        Args:
            name: Nombre del día.

        Returns:
            Nombre normalizado.
        """
        replacements = {
            "miercoles": "miércoles",
            "sabado": "sábado",
        }
        return replacements.get(name, name)

    def get_weekday_name(self, date_str: str) -> str:
        """
        Obtiene el nombre del día de la semana para una fecha.

        Args:
            date_str: Fecha en formato YYYY-MM-DD.

        Returns:
            Nombre del día en español o cadena vacía si falla.
        """
        try:
            date_obj = datetime.strptime(date_str, self.date_format)
            reverse_map = {v: k for k, v in self.weekdays.items()}
            return reverse_map.get(date_obj.weekday(), "")
        except Exception:
            return ""