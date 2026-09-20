# src/core/bot.py
"""
Bot de Telegram del Secretario IA.

Conecta todos los módulos y gestiona los comandos del usuario.
"""

import logging
from pathlib import Path
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

from src.core.config import Config
from src.modules.agenda import AgendaManager
from src.modules.study import StudyManager
from src.modules.llm import LLMClient
from src.utils.date_parser import DateParser

logger = logging.getLogger(__name__)


class SecretarioBot:
    """
    Bot principal del Secretario IA.

    Ejemplo:
        config = Config()
        bot = SecretarioBot(config)
        bot.run()
    """

    def __init__(self, config: Config):
        """Inicializa el bot con todos sus módulos."""
        self.config = config
        self.token = config.get("telegram.token")

        if not self.token:
            raise ValueError(
                "❌ No se encontró el token de Telegram. "
                "Configúralo en el archivo .env"
            )

        # Inicializar módulos
        self.date_parser = DateParser(config.get("agenda", {}))
        self.llm = LLMClient(config.get("llm", {}))
        self.agenda = AgendaManager(config.get_all(), self.date_parser)
        self.study = StudyManager(config.get_all())

        # Configurar aplicación
        self.app = (
            Application.builder()
            .token(self.token)
            .connect_timeout(60)
            .read_timeout(60)
            .build()
        )
        self._setup_handlers()

    def _setup_handlers(self):
        """Registra todos los comandos del bot."""
        self.app.add_handler(CommandHandler("start", self.cmd_start))
        self.app.add_handler(CommandHandler("help", self.cmd_start))
        self.app.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_text)
        )

    async def cmd_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Muestra el mensaje de bienvenida y los comandos."""
        mensaje = (
            "🤖 **Secretario IA V3**\n\n"
            "📌 **Comandos disponibles:**\n"
            "• `Agenda [tarea] para [materia] el [fecha]`\n"
            "• `¿Qué tengo hoy?`\n"
            "• `Completa [tarea]`\n"
            "• `Elimina [tarea]`\n\n"
            "📅 **Fechas:** 'jueves', '16', 'mañana', '2026-09-20'"
        )
        await update.message.reply_text(mensaje)

    async def handle_text(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Procesa los mensajes de texto del usuario."""
        mensaje = update.message.text
        logger.info(f"📩 Mensaje recibido: {mensaje}")

        # Interpretar con el LLM
        comando = self.llm.interpretar(mensaje)
        accion = comando.get("accion")

        if accion == "agendar":
            resultado = self.agenda.add_task(
                comando.get("tarea", ""),
                comando.get("materia", "General"),
                comando.get("fecha", "hoy"),
            )
        elif accion == "consultar":
            resultado = self._format_tasks(
                self.agenda.get_tasks(comando.get("filtro", "hoy"))
            )
        elif accion == "completar":
            resultado = self.agenda.complete_task(comando.get("tarea", ""))
        else:
            resultado = {
                "success": True,
                "message": "❓ No entendí el comando. Prueba con:\n"
                "• 'Agenda tarea para materia el jueves'\n"
                "• '¿Qué tengo hoy?'",
            }

        await update.message.reply_text(resultado.get("message", "✅"))

    def _format_tasks(self, result: Dict) -> Dict:
        """Formatea la lista de tareas para Telegram."""
        if not result.get("success") or result.get("count", 0) == 0:
            return {"success": True, "message": "📭 No hay tareas pendientes"}

        mensaje = "📋 **Tareas:**\n\n"
        for task in result["tasks"]:
            mensaje += f"• **{task['title']}** ({task.get('date', '')})\n"

        return {"success": True, "message": mensaje}

    def run(self):
        """Inicia el bot."""
        logger.info("🚀 Iniciando Secretario IA V3...")
        self.app.run_polling()