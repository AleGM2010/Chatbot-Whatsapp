# 🤖 Bot WhatsApp Web con Playwright

Un bot modular y extensible que utiliza [Playwright](https://playwright.dev/) para conectarse a WhatsApp Web y automatizar respuestas a mensajes entrantes. Ideal para automatización de atención al cliente, respuestas simples y prototipos rápidos.

## 📦 Características principales

- Interacción con WhatsApp Web mediante Playwright (async).
- Arquitectura modular con interfaces desacopladas para facilitar personalización.
- Sistema de respuestas personalizables por cliente.
- Cache de mensajes para evitar procesar mensajes duplicados.
- Preparado para empaquetarse como módulo instalable con `pyproject.toml`.

## 📁 Estructura del proyecto

```plaintext´´´
bot_whatsapp/
├── __init__.py
├── browser.py
├── interface.py
├── logic.py
├── cache.py
├── bot.py
└── scripts/
    ├── __init__.py
    └── run_bot.py
pyproject.toml
README.md
```

# 🧰 Requisitos

Python 3.10 o superior
Un navegador compatible con Playwright (se instala automáticamente con playwright install)

Dependencias:

playwright
Otras especificadas en pyproject.toml



## 🚀 Instalación (Crea una carpeta contenedora primero)

```bash
git clone https://github.com/AleGM2010/bot-whatsapp.git
python -m venv venv
venv\Scripts\activate
pip install -e .
playwright install
```

## Ejecuta el bot en la terminal con UNO de estos
- run-bot
- python bot_whatsapp/scripts/run_bot.py

# 🛠️ Uso del programa

- Ejecuta el script run_bot.py.
- Escanea el código QR que aparece en WhatsApp Web cuando se abra el navegador.
- Presiona ENTER después de escanear el QR.
- Selecciona manualmente el chat que deseas monitorear y presiona ENTER.
- El bot responderá automáticamente a los mensajes entrantes según las reglas definidas en logic.py.


## 🔧 Personalización

Respuestas personalizadas: Crea una nueva clase que herede de IResponseLogic en logic.py para definir respuestas específicas por cliente.

Interfaz alternativa: Implementa una nueva clase para IWhatsAppInterface en interface.py para soportar otras plataformas o métodos de interacción.


[!NOTE]
Asegúrate de mantener el entorno virtual activo mientras ejecutas el bot para evitar problemas con las dependencias.
