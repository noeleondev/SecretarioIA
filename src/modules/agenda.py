# src/modules/agenda.py
"""
Módulo de gestión de agenda.

Crea, lee, completa y elimina tareas en formato Markdown dentro
del Vault de Obsidian.
"""

import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)


class AgendaManager:
    """
    Gestor de tareas en Obsidian.

    Ejemplo:
        agenda = AgendaManager(config)
        resultado = agenda.add_task("Estudiar", "Cálculo", "jueves")
    """

    def __init__(self, config: dict, date_parser=None):
        """
        Inicializa el gestor.

        Args:
            config: Configuración con la ruta del Vault.
            date_parser: Parser de fechas (opcional).
        """
        self.config = config
        self.vault_path = Path(config.get("paths", {}).get("vault", "./data/vault"))
        self.vault_path.mkdir(parents=True, exist_ok=True)
        self.date_parser = date_parser

    def add_task(self, title: str, subject: str, date_text: str) -> Dict:
        """
        Agrega una nueva tarea.

        Args:
            title: Título de la tarea.
            subject: Materia.
            date_text: Texto de fecha (ej. "jueves").

        Returns:
            Diccionario con el resultado.
        """
        try:
            # Parsear fecha
            date_str = (
                self.date_parser.parse(date_text)
                if self.date_parser
                else date_text
            )
            if not date_str:
                return {
                    "success": False,
                    "message": f"❌ No entendí la fecha: '{date_text}'",
                }

            # Sanitizar nombre
            safe_title = re.sub(r'[<>:"/\\|?*]', "", title)[:50].strip()
            filename = f"{date_str} - {safe_title}.md"
            filepath = self.vault_path / filename

            if filepath.exists():
                return {
                    "success": False,
                    "message": f"⚠️ La tarea ya existe: {title}",
                }

            # Crear contenido
            content = self._generate_markdown(title, subject, date_str)
            filepath.write_text(content, encoding="utf-8")

            return {
                "success": True,
                "message": f"✅ Tarea agendada: {title} ({date_str})",
                "task": {"title": title, "subject": subject, "date": date_str},
            }

        except Exception as e:
            logger.error(f"❌ Error al agregar tarea: {e}")
            return {"success": False, "message": f"❌ Error: {e}"}

    def get_tasks(self, filter_type: str = "hoy") -> Dict:
        """
        Obtiene las tareas según un filtro.

        Args:
            filter_type: "hoy", "semana", "todas".

        Returns:
            Diccionario con las tareas encontradas.
        """
        try:
            tasks = []
            today = datetime.now().date()

            for filepath in self.vault_path.glob("*.md"):
                task = self._parse_task(filepath)
                if not task or task.get("status") == "completada":
                    continue

                # Aplicar filtro
                if filter_type == "todas":
                    tasks.append(task)
                else:
                    task_date = datetime.strptime(
                        task["date"], "%Y-%m-%d"
                    ).date()
                    days_diff = (task_date - today).days

                    if filter_type == "hoy" and days_diff == 0:
                        tasks.append(task)
                    elif filter_type == "semana" and 0 <= days_diff <= 7:
                        tasks.append(task)

            tasks.sort(key=lambda x: x.get("date", ""))
            return {"success": True, "count": len(tasks), "tasks": tasks}

        except Exception as e:
            logger.error(f"❌ Error al obtener tareas: {e}")
            return {"success": False, "message": f"❌ Error: {e}"}

    def complete_task(self, query: str) -> Dict:
        """
        Marca una tarea como completada.

        Args:
            query: Texto a buscar.

        Returns:
            Diccionario con el resultado.
        """
        try:
            query = query.lower().strip()
            for filepath in self.vault_path.glob("*.md"):
                content = filepath.read_text(encoding="utf-8")
                if query in content.lower() and "Completada" not in content:
                    content = content.replace("Pendiente", "Completada")
                    filepath.write_text(content, encoding="utf-8")
                    return {
                        "success": True,
                        "message": f"✅ Tarea completada: {filepath.stem}",
                    }

            return {
                "success": False,
                "message": f"❌ No encontré tarea pendiente con: '{query}'",
            }

        except Exception as e:
            logger.error(f"❌ Error al completar tarea: {e}")
            return {"success": False, "message": f"❌ Error: {e}"}

    def _generate_markdown(self, title: str, subject: str, date: str) -> str:
        """Genera el contenido Markdown de una tarea."""
        return f"""# {title}

**Fecha:** {date}
**Materia:** {subject}
**Estado:** Pendiente

---
*Creado: {datetime.now().strftime('%Y-%m-%d %H:%M')}*
"""

    def _parse_task(self, filepath: Path) -> Optional[Dict]:
        """Parsea un archivo Markdown y extrae los datos de la tarea."""
        try:
            content = filepath.read_text(encoding="utf-8")
            task = {"filename": filepath.stem}

            for line in content.split("\n"):
                if line.startswith("# "):
                    task["title"] = line[2:].strip()
                elif "**Fecha:**" in line:
                    task["date"] = line.split("**Fecha:**")[1].strip()
                elif "**Materia:**" in line:
                    task["subject"] = line.split("**Materia:**")[1].strip()
                elif "**Estado:**" in line:
                    task["status"] = (
                        "completada"
                        if "Completada" in line
                        else "pendiente"
                    )

            return task if "title" in task and "date" in task else None

        except Exception:
            return None