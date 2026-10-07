# Limitaciones del Agente Local (Bionic + OxCoder 9B)

**Fecha:** 2026-10-06

## Contexto

Se probó usar Bionic con OxCoder 9B para auditar el repositorio SecretarioIA.
El agente tenía acceso a la carpeta, pero falló en tareas básicas de lectura.

## Hallazgos

### 1. Loop de exploración shell
Al pedirle "busca el README", el agente entró en un bucle de comandos (ls, find, cat)
sin encontrar el archivo, hasta que se le dio la ruta exacta.

### 2. Comandos shell no funcionales en Git Bash
ls, head y cat fallaron. El agente no intentó alternativas
(python -c, type, Get-Content) y declaró bloqueo externo.

### 3. Asimetría de herramientas
list_dir funciona, pero no hay herramienta de lectura de archivos equivalente.
El modelo no improvisa una solución.

### 4. Obediencia literal
Al pedir "lee solo el repo", omitió todo lo demás sin inferir contexto.
No tiene modelo mental de la estructura del proyecto.

## Mitigación aplicada

Se creó CONTEXT.md en la raíz con:
- Índice explícito de rutas de archivos.
- Reglas para el agente (no explorar, usar rutas dadas).
- Convenciones del proyecto.

## Recomendaciones

1. No usar modelos menores a 14B como agentes autónomos.
2. Probar Qwen2.5-Coder-7B-Instruct (mejor tool-use).
3. Diseñar prompts asumiendo herramientas asimétricas.
4. Toda lectura de archivo debe indicar ruta absoluta.
