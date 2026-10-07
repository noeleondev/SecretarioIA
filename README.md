# Secretario IA V3

Asistente personal de IA **parcialmente local** para gestión de agenda y estudio.

> AVISO IMPORTANTE: Este proyecto NO es 100% offline.
> Requiere conexión a internet para Telegram y para sincronización vía Syncthing.
> Solo el procesamiento de IA (LM Studio) es local.

---

## Descripcion honesta

Secretario IA es un asistente que usa modelos de IA locales (a traves de LM Studio)
para gestionar tareas y organizar apuntes en Markdown.

### Estado actual: EN DESARROLLO - NO FUNCIONAL

- La carpeta src/ esta vacia.
- No hay bot funcional implementado.
- Este README documenta la intencion del proyecto, no lo que existe hoy.
- Ver STATUS.md para el estado real.

---

## Caracteristicas PLANIFICADAS (no implementadas)

| Caracteristica | Estado |
|---|---|
| Gestion de agenda via Telegram | Planificado |
| Organizacion de apuntes en Markdown | Planificado |
| IA local con LM Studio | Configurado (sin integracion) |
| Sistema de estudio guiado | Planificado |
| Transcripcion de voz con Whisper | Planificado |
| Sincronizacion multi-dispositivo | Via Syncthing (requiere internet) |

---

## Requisitos reales de conectividad

| Funcion | Requiere internet? |
|---|---|
| Procesamiento de IA (LM Studio) | No |
| Envio/recepcion de Telegram | Si |
| Sincronizacion con Syncthing | Si |
| Descarga de modelos | Si (solo la primera vez) |

---

## Requisitos de Hardware

| Componente | Minimo | Recomendado |
|---|---|---|
| CPU | Gama 5 (Intel i5 / Ryzen 5) | Gama 7 (Intel i7 / Ryzen 7) |
| RAM | 16 GB | 32 GB |
| Almacenamiento | 10 GB libres | 20 GB libres |
| GPU | Integrada | Dedicada (opcional) |

---

## Estado del desarrollo

Este repositorio esta PAUSADO desde el 2026-10-06.
Ver STATUS.md para detalles y proximos pasos.

Las secciones de instalacion y uso del README original se conservan en
README.md.bak como referencia de la INTENCION del proyecto, pero NO
describen funcionalidad actual.

---

## Lecciones aprendidas

Documentadas en docs/agent-limitations.md.

---

Si el proyecto te interesa, revisa STATUS.md antes de clonar.
