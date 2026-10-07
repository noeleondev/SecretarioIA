# Status: Pausado

**Fecha de pausa:** 2026-10-06
**Razón:** Pivote estratégico a aprendizaje de fundamentos (Git, Python, Bionic) antes de continuar desarrollo.

## Estado real del proyecto

- El proyecto NO es 100% offline. Requiere internet para:
  - Telegram (envio/recepcion de mensajes)
  - Syncthing (sincronizacion entre dispositivos)
- El procesamiento de IA si es local (LM Studio).
- Existe codigo en src/ (~35 KB) con arquitectura modular:
  - src/core/: bot, config, logger
  - src/modules/: agenda, llm, study
  - src/utils/: date_parser, validators
- El codigo NO esta verificado end-to-end. No hay evidencia de que el bot arranque sin errores.
- Encoding de algunos archivos esta roto (UTF-8 mal decodificado como Latin-1).

## Lo que SI funciona

- Configuracion de LM Studio para hardware sin GPU dedicada.
- Estructura de carpetas y scripts de instalacion (setup.bat, run.bat).
- Documentacion de usuario en el historial de Git (ver commit b362656).
- Esqueleto de codigo Python con modulos separados por responsabilidad.

## Lo que NO esta verificado / puede no funcionar

- Arranque del bot via python src/main.py (sin probar).
- Integracion real con LM Studio (cliente definido, sin test).
- Integracion con Obsidian (solo carpeta creada).
- Sistema de estudio guiado (modulo existe, sin probar).
- Transcripcion de voz (dependencias listadas, sin integracion).
- Encoding UTF-8 de los archivos .py (roto en varios).

## Lecciones aprendidas

Ver docs/agent-limitations.md.

## Proximos pasos (al retomar)

1. Corregir encoding UTF-8 de todos los archivos en src/.
2. Probar python src/main.py y documentar que falla.
3. Migrar de OxCoder 9B a Qwen2.5-Coder-7B-Instruct para asistencia.
4. Escribir tests para src/utils/date_parser.py (es el modulo mas testeable).
