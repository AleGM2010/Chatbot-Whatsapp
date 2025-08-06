import asyncio
from datetime import datetime
import platform
from bot_whatsapp.interfaces import IBrowserManager, IWhatsAppInterface, IResponseLogic, IMessageCache



# Orquestador
class WhatsAppBot:
    def __init__(self, browser_manager: IBrowserManager, whatsapp_interface: IWhatsAppInterface,
                 response_logic: IResponseLogic, message_cache: IMessageCache):
        self.browser_manager = browser_manager
        self.whatsapp_interface = whatsapp_interface
        self.response_logic = response_logic
        self.message_cache = message_cache
        self.hora_inicio = None

    def obtener_hora_actual(self):
        formato = "%H:%M, %-d/%-m/%Y" if platform.system() != "Windows" else "%H:%M, %#d/%#m/%Y"
        return datetime.now().strftime(formato)

    async def run(self):
        await self.browser_manager.start()
        page = await self.browser_manager.get_page()
        await self.whatsapp_interface.initialize(page)
        await self.whatsapp_interface.wait_for_user_click("Haz click en el chat para escuchar")
        await self.whatsapp_interface.send_message("hola! chatbot activado!")
        self.hora_inicio = self.obtener_hora_actual()
        await self.whatsapp_interface.show_initial_message()

        print("[INFO] Bot corriendo. Ctrl+C para detener.")
        try:
            while True:
                nuevos = await self.whatsapp_interface.get_new_messages(self.hora_inicio)
                for texto, key in nuevos:
                    if not self.message_cache.is_message_processed(key):
                        respuesta = self.response_logic.get_response(texto)
                        await self.whatsapp_interface.send_message(respuesta)
                        self.message_cache.add_message(key)
                        print(f"[INFO] Respondí a mensaje entrante: {texto}")
                await asyncio.sleep(5)
        except KeyboardInterrupt:
            print("[INFO] Interrupción manual recibida.")
        finally:
            await self.browser_manager.stop()
            print("[INFO] Bot detenido correctamente.")