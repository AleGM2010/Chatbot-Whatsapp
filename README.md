🤖 Bot WhatsApp Web con Playwright
Este es un bot modular y extensible que se conecta a WhatsApp Web usando Playwright para automatizar respuestas a mensajes entrantes. Ideal para atención automática, respuestas simples y prototipos.

📦 Características principales

Uso de Playwright (async) para interactuar con WhatsApp Web.
Arquitectura basada en interfaces desacopladas para facilitar personalización.
Sistema de respuesta personalizable por cliente.
Cache de mensajes para evitar duplicaciones.
Preparado para empaquetar como módulo instalable con pyproject.toml.


📁 Estructura del proyecto
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


🧰 Requisitos

Python 3.10+
Navegador instalado compatible con Playwright (se instala automáticamente con playwright install)
Dependencias:
playwright
Otras dependencias especificadas en pyproject.toml




🚀 Instalación y ejecución

Clonar el repositorio (o copiar tu proyecto en una carpeta):
git clone https://github.com/tuusuario/bot-whatsapp.git
cd bot-whatsapp


Crear entorno virtual e instalar dependencias:
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -e .
playwright install


Ejecutar el bot:
run-bot

O directamente con:
python bot_whatsapp/scripts/run_bot.py




🛠️ Uso

Ejecuta el script run_bot.py.
Escanea el código QR de WhatsApp Web cuando se abra el navegador.
Presiona ENTER tras escanear el QR.
Selecciona manualmente el chat que deseas monitorear y presiona ENTER.
El bot responderá automáticamente a los mensajes entrantes según las reglas definidas en logic.py.


🔧 Personalización

Respuestas personalizadas: Implementa una nueva clase que herede de IResponseLogic en logic.py para definir respuestas específicas por cliente.
Interfaz alternativa: Crea una nueva implementación de IWhatsAppInterface en interface.py para soportar otras
