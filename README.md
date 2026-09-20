# 📝 README.md COMPLETO Y ORDENADO

Copia **TODO** el contenido del bloque de abajo y pégalo en tu `README.md`:

```markdown
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

## 💻 Requisitos de Hardware

| Componente | Mínimo | Recomendado |
|------------|--------|-------------|
| **CPU** | Gama 5 (Intel i5 / Ryzen 5) | Gama 7 (Intel i7 / Ryzen 7) |
| **RAM** | 16 GB | 32 GB |
| **Almacenamiento** | 10 GB libres | 20 GB libres |
| **GPU** | Integrada | Dedicada (opcional) |

---

## 🚀 Instalación Completa (Paso a Paso)

### 📦 Paso 1: Instalar Python 3.11.9

**Descarga:** [python.org](https://www.python.org/downloads/release/python-3119/)

1. Ve al enlace de descarga.
2. Busca **"Windows installer (64-bit)"** y descárgalo.
3. Ejecuta el instalador.
4. ⚠️ **MUY IMPORTANTE:** Marca la casilla **"Add python.exe to PATH"**.
5. Haz clic en **"Install Now"**.
6. Espera a que termine (2-3 minutos).
7. Haz clic en **"Close"**.

**Verifica la instalación:**

Abre una **nueva ventana de CMD** (importante: nueva) y escribe:

```bash
python --version
```

Debe mostrar:
```
Python 3.11.9
```

---

### 📦 Paso 2: Instalar Git

**Descarga:** [git-scm.com](https://git-scm.com/download/win)

1. Ve al enlace de descarga.
2. Descarga **"64-bit Git for Windows Setup"**.
3. Ejecuta el instalador.
4. Deja todas las opciones por defecto.
5. Haz clic en **"Install"**.
6. Espera a que termine.
7. Haz clic en **"Finish"**.

**Verifica la instalación:**

Abre una **nueva ventana de CMD** y escribe:

```bash
git --version
```

Debe mostrar algo como:
```
git version 2.46.0.windows.1
```

---

### 📦 Paso 3: Instalar LM Studio

**Descarga:** [lmstudio.ai](https://lmstudio.ai/)

1. Ve al enlace de descarga.
2. Descarga la versión para Windows.
3. Ejecuta el instalador.
4. Sigue las instrucciones.
5. Abre LM Studio.

**Descargar el modelo:**

1. En LM Studio, haz clic en la pestaña **"Search"** (lupa).
2. En la barra de búsqueda, escribe: **`Qwen3-4B-2507`**
3. Selecciona el modelo que aparece.
4. Haz clic en **"Download"**.
5. Espera a que termine la descarga (aproximadamente 2.5 GB).

**Iniciar el servidor:**

1. Ve a la pestaña **"Server"** (icono de servidor).
2. Haz clic en **"Start Server"**.
3. Debe decir: `Server running on http://localhost:1234`

> ⚠️ **IMPORTANTE:** LM Studio debe estar abierto y con el servidor activo **cada vez que uses el bot**.

---

### 📦 Paso 4: Clonar el repositorio

Abre **CMD** y escribe:

```bash
cd C:\Users\TU_USUARIO\Documents
git clone https://github.com/noeleondev/SecretarioIA.git
cd SecretarioIA\Scripts
```

> **Nota:** Reemplaza `TU_USUARIO` con tu nombre de usuario de Windows.

**Deberías ver:**

```
Cloning into 'SecretarioIA'...
remote: Enumerating objects: 100, done.
...
Receiving objects: 100% (100/100), 50.00 KiB | 500 KiB/s, done.
```

---

### 📦 Paso 5: Ejecutar la configuración inicial

Dentro de la carpeta `Scripts`, ejecuta:

**Windows:**
```bash
setup.bat
```

**Linux / Mac:**
```bash
chmod +x run.sh
./run.sh
```

**¿Qué hace este script?**

- ✅ Verifica que Python esté instalado.
- ✅ Crea el entorno virtual (`venv/`).
- ✅ Instala todas las dependencias.
- ✅ Crea el archivo `.env` desde `.env.example`.
- ✅ Abre el `.env` en el Bloc de notas.
- ✅ Crea la carpeta `Almacenamiento/vault`.

**Deberías ver:**

```
==========================================
  CONFIGURACION INICIAL - SECRETARIO IA V3
==========================================

[1/5] Verificando Python...
[OK] Python encontrado.
[2/5] Creando entorno virtual...
[OK] Entorno virtual creado.
[3/5] Instalando dependencias...
[OK] Dependencias instaladas.
[4/5] Configurando variables de entorno...
[OK] Archivo .env creado desde .env.example.

==========================================
  IMPORTANTE: CONFIGURA TU TOKEN
==========================================

Se abrira el archivo .env en el Bloc de notas.
Por favor, reemplaza:
    AQUI_VA_TU_TOKEN_DE_TELEGRAM
por tu token real de Telegram.

Presione una tecla para continuar...
```

---

### 📦 Paso 6: Configurar el token de Telegram

**El script `setup.bat` abrirá automáticamente el Bloc de notas con el archivo `.env`.**

**Si NO tienes un token de Telegram, sigue estos pasos:**

1. Abre **Telegram** en tu celular o PC.
2. En la barra de búsqueda, escribe: **`@BotFather`**
3. Haz clic en el resultado (tiene un check azul de verificación).
4. Envía el comando: **`/newbot`**
5. BotFather te pedirá un nombre. Escribe: **`Mi Secretario IA`**
6. BotFather te pedirá un usuario. Escribe algo como: **`mi_secretario_bot`** (debe terminar en `_bot`).
7. BotFather te dará un **token**. Se ve así:

```
8793105577:AAF8308YNEIgVyG2X0Csbyasg7cvWrFSGZA
```

8. **Copia ese token.**

**Ahora, en el Bloc de notas:**

1. Busca la línea:
   ```
   TELEGRAM_TOKEN=AQUI_VA_TU_TOKEN_DE_TELEGRAM
   ```
2. Reemplázala por:
   ```
   TELEGRAM_TOKEN=8793105577:AAF8308YNEIgVyG2X0Csbyasg7cvWrFSGZA
   ```
   (Con TU token real)
3. Guarda (Ctrl + S).
4. Cierra el Bloc de notas.

---

### 📦 Paso 7: Ejecutar el bot

En la misma terminal, ejecuta:

**Windows:**
```bash
run.bat
```

**Linux / Mac:**
```bash
./run.sh
```

**Deberías ver:**

```
==========================================
   SECRETARIO IA V3
==========================================

[INFO] Activando entorno virtual...
[INFO] Verificando dependencias...
[INFO] Iniciando el bot...
==================================================
🤖 SECRETARIO IA V3
==================================================
✅ Configuración cargada
✅ Sistema de logs iniciado
✅ Bot iniciado
==================================================
Presiona Ctrl+C para detener
==================================================
```

**¡El bot está funcionando!**

---

### 📦 Paso 8: Probar el bot en Telegram

1. Abre **Telegram**.
2. Busca tu bot por su nombre de usuario (ej. `@mi_secretario_bot`).
3. Envía el comando: **`/start`**

**Debería responder:**

```
🤖 Secretario IA V3

📌 Comandos disponibles:
• Agenda [tarea] para [materia] el [fecha]
• ¿Qué tengo hoy?
• Completa [tarea]
• Elimina [tarea]

📅 Fechas: 'jueves', '16', 'mañana', '2026-09-20'
```

**Ahora prueba agendar una tarea:**

```
Agenda estudiar cálculo para matemáticas el jueves
```

**Debería responder:**

```
✅ Tarea agendada: estudiar cálculo (2026-09-24)
```

**¡Felicidades! El bot está funcionando correctamente.**

---

## 🎮 Cómo Usar el Bot

### 📅 Comandos de Agenda

#### 1. Agendar una tarea

**Formato:**
```
Agenda [tarea] para [materia] el [fecha]
```

**Ejemplos:**
| Lo que escribes | Lo que hace |
|-----------------|-------------|
| `Agenda estudiar cálculo para matemáticas el jueves` | Agenda la tarea "estudiar cálculo" de "matemáticas" para el próximo jueves |
| `Agenda investigar PostgreSQL para BD el 16` | Agenda la tarea "investigar PostgreSQL" de "BD" para el día 16 |
| `Agenda practicar inglés para Inglés el mañana` | Agenda la tarea "practicar inglés" para mañana |
| `Agenda examen final para Física el viernes 20` | Agenda la tarea "examen final" para el viernes 20 |

**Formatos de fecha soportados:**
| Formato | Significado |
|---------|-------------|
| `hoy` | Hoy |
| `mañana` | Mañana |
| `pasado mañana` | Pasado mañana |
| `jueves`, `viernes`, etc. | Próximo día de la semana |
| `16` | Día 16 del mes actual |
| `jueves 16` | Jueves 16 del mes actual |
| `2026-09-20` | Fecha específica |

---

#### 2. Consultar tareas de hoy

**Lo que escribes:**
```
¿Qué tengo hoy?
```

**Lo que responde:**
```
📋 Tareas de hoy:

• estudiar cálculo (2026-09-24)
• investigar PostgreSQL (2026-09-16)
```

---

#### 3. Consultar tareas de la semana

**Lo que escribes:**
```
Tareas de la semana
```

**Lo que responde:**
```
📋 Tareas de la semana:

• estudiar cálculo (2026-09-24)
• investigar PostgreSQL (2026-09-16)
• examen final (2026-09-20)
```

---

#### 4. Ver todas las tareas

**Lo que escribes:**
```
Ver agenda
```

**Lo que responde:**
```
📋 Lista de tareas pendientes:

• estudiar cálculo (2026-09-24)
• investigar PostgreSQL (2026-09-16)
• examen final (2026-09-20)
```

---

#### 5. Completar una tarea

**Formato:**
```
Completa [descripción de la tarea]
```

**Ejemplos:**
| Lo que escribes | Lo que hace |
|-----------------|-------------|
| `Completa estudiar` | Marca la tarea "estudiar cálculo" como completada |
| `Completa investigar` | Marca la tarea "investigar PostgreSQL" como completada |

**Lo que responde:**
```
✅ Tarea completada: estudiar cálculo
```

---

#### 6. Eliminar una tarea

**Formato:**
```
Elimina [descripción de la tarea]
```

**Ejemplos:**
| Lo que escribes | Lo que hace |
|-----------------|-------------|
| `Elimina estudiar` | Elimina la tarea "estudiar cálculo" |
| `Elimina investigar` | Elimina la tarea "investigar PostgreSQL" |

**Lo que responde:**
```
🗑️ Tarea eliminada: estudiar cálculo
```

---

### 🎙️ Comandos de Voz

También puedes enviar **mensajes de voz** en lugar de texto. El bot los transcribirá automáticamente con Whisper.

**Ejemplo:**
1. Grabas un mensaje de voz diciendo: "Agenda estudiar cálculo para matemáticas el jueves"
2. Envías el mensaje de voz
3. El bot responde:
   ```
   📝 Dijiste: 'Agenda estudiar cálculo para matemáticas el jueves'
   ✅ Tarea agendada: estudiar cálculo (2026-09-24)
   ```

> **Nota:** Los mensajes de voz requieren que configures FFmpeg en el archivo `.env`.

---

### 🎓 Comandos de Estudio (En desarrollo)

| Comando | Ejemplo | Qué hace |
|---------|---------|----------|
| **Organizar libro** | `/organizar ingles nivel0.txt` | Organiza un libro en temas |
| **Ver índice** | `/indice ingles` | Muestra los temas disponibles |
| **Empezar tema** | `/empezar ingles El_alfabeto` | Inicia una sesión de estudio |
| **Progreso** | `/progreso ingles` | Muestra el progreso |

> **Nota:** Los comandos de estudio están en desarrollo y pueden cambiar.

---

## 📁 Estructura del Proyecto

```
SecretarioIA/
├── Almacenamiento/          # Bóveda de Obsidian (no se sube a Git)
│   └── vault/               # Tus apuntes
│
└── Scripts/                 # Código del bot (esto se sube a Git)
    ├── config/              # Archivos de configuración
    ├── data/                # Datos del bot
    ├── docs/                # Documentación
    ├── logs/                # Registros (no se suben)
    ├── src/                 # Código fuente
    ├── tests/               # Tests
    ├── .env.example         # Plantilla de variables de entorno
    ├── .gitignore           # Archivos ignorados por Git
    ├── README.md            # Este archivo
    ├── requirements.txt     # Dependencias
    ├── run.bat              # Script de inicio (Windows)
    ├── run.sh               # Script de inicio (Linux/Mac)
    └── setup.bat            # Script de configuración inicial
```

---

## ❓ Preguntas Frecuentes

### ¿Cada vez que quiera usar el bot tengo que hacer todo esto?

**No.** Solo la primera vez. Después, solo necesitas:

1. Abrir LM Studio y activar el servidor.
2. Hacer doble clic en `run.bat`.

### ¿Qué pasa si cierro la terminal?

El bot se detiene. Para volver a iniciarlo, ejecuta `run.bat` de nuevo.

### ¿Puedo mover la carpeta a otra ubicación?

**Sí.** Los scripts son portátiles. Funcionan en cualquier carpeta. Solo asegúrate de que `Almacenamiento` esté al mismo nivel que `Scripts`.

### ¿Cómo agrego más modelos?

1. Descárgalos en LM Studio.
2. Edita el archivo `.env` y cambia la línea:
   ```
   LM_STUDIO_MODEL=NombreDelNuevoModelo
   ```

### ¿Cómo desinstalo todo?

1. Borra la carpeta `SecretarioIA`.
2. Desinstala Python, Git, LM Studio.
3. Listo.

### ¿Dónde se guardan mis tareas?

Las tareas se guardan en la carpeta `Almacenamiento/vault/` como archivos Markdown. Puedes abrirlos con Obsidian o cualquier editor de texto.

### ¿Puedo usar Obsidian para ver mis tareas?

**Sí.** Obsidian es una aplicación de notas que lee archivos Markdown. Abre la carpeta `Almacenamiento/vault/` como bóveda en Obsidian.

---

## 🤝 Contribuir

Si eres parte del equipo, revisa la [guía de contribución](docs/08_CONTRIBUTING.md).

### Reglas básicas

1. **Nunca subas tu `.env`** a GitHub.
2. **Nunca subas la carpeta `venv/`** a GitHub.
3. **Crea una rama nueva** para cada funcionalidad:
   ```bash
   git checkout -b feature/nombre-de-tu-funcionalidad
   ```
4. **Haz commits descriptivos**:
   ```
   feat: agrego comando X
   fix: corrijo error en Y
   docs: actualizo documentación Z
   ```
5. **Haz un Pull Request** cuando termines.
6. **Espera la revisión del líder** antes de fusionar.

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**. Ver el archivo [LICENSE](LICENSE)
para más detalles.

---

## 👥 Autores

- **noeleondev** — Creador y líder del proyecto
- [Añade aquí a tus compañeros]

---

## ⭐ Agradecimientos

- A **LM Studio** por hacer posible la IA local.
- A **Obsidian** por ser una herramienta increíble de notas.
- A **Python** y su comunidad.
- A todos los que contribuyan a este proyecto.

---

**⭐ Si te gusta el proyecto, dale una estrella en GitHub!**
```
