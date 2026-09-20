# 🤖 Secretario IA V3

Asistente personal de IA local y gratuito para gestión de agenda y estudio.

[![Estado](https://img.shields.io/badge/estado-en%20desarrollo-yellow)]()
[![Licencia](https://img.shields.io/badge/licencia-MIT-blue)]()
[![Python](https://img.shields.io/badge/python-3.11.9-blue)]()

---

## 📖 Descripción

**Secretario IA** es un asistente personal que funciona **100% offline** en tu PC.
Usa modelos de IA locales (a través de **LM Studio**) para gestionar tus tareas,
organizar tus apuntes y ayudarte a estudiar.

Este proyecto nació como una herramienta personal y ahora es un **proyecto
comunitario** para aprender a trabajar en equipo con Git, GitHub y desarrollo
colaborativo.

---

## ✨ Características

- 📅 **Gestión de agenda**: Crea, consulta y completa tareas.
- 📚 **Organización de libros**: Extrae la estructura de tus apuntes en Markdown.
- 🧠 **IA local**: Usa LM Studio con modelos como `Qwen3-4B-2507`.
- 🎓 **Sistema de estudio**: Divide temas en pasos pequeños y te guía.
- 🔒 **100% offline**: Tus datos nunca salen de tu PC.
- 🤝 **Comunitario**: Diseñado para colaborar con compañeros.

---

## 📋 Requisitos

### Hardware mínimo

| Componente | Mínimo | Recomendado |
|------------|--------|-------------|
| **CPU** | Gama 5 (Intel i5 / Ryzen 5) | Gama 7 (Intel i7 / Ryzen 7) |
| **RAM** | 16 GB | 32 GB |
| **Almacenamiento** | 10 GB libres | 20 GB libres |
| **GPU** | Integrada | Dedicada (opcional) |

### Software

| Software | Versión | ¿Obligatorio? | Descarga |
|----------|---------|---------------|----------|
| **Python** | 3.11.9 | ✅ Sí | [python.org](https://www.python.org/downloads/release/python-3119/) |
| **Git** | Última | ✅ Sí | [git-scm.com](https://git-scm.com/) |
| **LM Studio** | Última | ✅ Sí | [lmstudio.ai](https://lmstudio.ai/) |
| **Obsidian** | Última | ✅ Sí | [obsidian.md](https://obsidian.md/) |
| **FFmpeg** | Última | 🟡 Opcional | [ffmpeg.org](https://ffmpeg.org/) |

---

## 🚀 Instalación Rápida

### Windows

1. **Configurar** (solo la primera vez):
   - Haz doble clic en `setup.bat`
   - Espera a que termine
   - Edita el archivo `.env` con tus datos (te lo pedirá el script)

2. **Ejecutar** el bot:
   - Haz doble clic en `run.bat`

### Linux / Mac

1. **Configurar** (solo la primera vez):
   ```bash
   chmod +x run.sh
   ./run.sh