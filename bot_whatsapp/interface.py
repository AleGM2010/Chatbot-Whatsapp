

from bot_whatsapp.interfaces import IWhatsAppInterface

class DefaultWhatsAppInterface(IWhatsAppInterface):
    def __init__(self):
        self.page = None

    async def initialize(self, page):
        self.page = page

    async def send_message(self, text):
        print(f"[DEBUG] Intentando enviar mensaje: {text}")
        input_box = await self.page.wait_for_selector("div[contenteditable='true'][aria-label='Escribe un mensaje']")
        await input_box.fill(text)
        await input_box.press("Enter")
        print("[INFO] Mensaje enviado.")

    async def wait_for_user_click(self, message):
        print(f"[INTERACCIÓN MANUAL] {message}")
        print("Luego presiona ENTER para continuar...")
        input()
        print("[INFO] Continuando...")

    async def get_new_messages(self, start_time):
        mensajes = []
        selector = ".message-in:not(.message-out) .copyable-text[data-pre-plain-text]"
        elements = await self.page.query_selector_all(selector)
        print(f"[DEBUG] Mensajes encontrados: {len(elements)}")
        for el in elements:
            texto_el = await el.query_selector("span.selectable-text, p")
            texto = await texto_el.inner_text() if texto_el else None
            hora = await el.get_attribute("data-pre-plain-text")
            msg_id = await el.get_attribute("data-id")
            if texto and hora:
                hora = hora.split(']')[0].lstrip('[')
                if hora < start_time:
                    continue
                key = f"{msg_id}|{hora}|{texto}" if msg_id else f"{hora}|{texto}"
                mensajes.append((texto, key))
                print(f"[DEBUG] Nuevo mensaje detectado: {texto} con key: {key}")
        print(f"[DEBUG] Nuevos mensajes detectados: {len(mensajes)}")
        return mensajes

    async def show_initial_message(self):
        selector = ".message-in .copyable-text[data-pre-plain-text]"
        elements = await self.page.query_selector_all(selector)
        if elements:
            ultimo = elements[-1]
            texto_el = await ultimo.query_selector("span.selectable-text, p")
            texto = await texto_el.inner_text() if texto_el else ""
            print(f"[INFO] Último mensaje entrante detectado al iniciar: {texto}")
        else:
            print("[INFO] No se detectó ningún mensaje entrante al iniciar.")