# scripts/run_bot.py
from bot_whatsapp.browser import DefaultBrowserManager
from bot_whatsapp.interface import DefaultWhatsAppInterface
from bot_whatsapp.logic import DefaultResponseLogic
from bot_whatsapp.cache import DefaultMessageCache
from bot_whatsapp.bot import WhatsAppBot
import asyncio

def main():
    bot = WhatsAppBot(
        browser_manager=DefaultBrowserManager(),
        whatsapp_interface=DefaultWhatsAppInterface(),
        response_logic=DefaultResponseLogic(),
        message_cache=DefaultMessageCache()
    )
    asyncio.run(bot.run())
