
import sys
import asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
from bot_whatsapp.interfaces import IBrowserManager


# Implementaciones genéricas
class DefaultBrowserManager(IBrowserManager):
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    async def start(self):
        try:
            self.playwright = await async_playwright().start()
            self.browser = await self.playwright.chromium.launch(headless=False)
            self.page = await self.browser.new_page()
            await self.page.goto("https://web.whatsapp.com")
            print("[INFO] Escaneá el QR en WhatsApp Web...")
            input("[INFO] Presiona ENTER cuando hayas escaneado el QR y estés dentro...")
            posibles_selectores = [
                "#app",
                "div[contenteditable='true'][data-tab]",
                "[data-pre-plain-text]",
                "[aria-label='Menú']"
            ]
            tasks = [asyncio.create_task(self.page.wait_for_selector(sel, timeout=180000)) for sel in posibles_selectores]
            done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
            for task in pending:
                task.cancel()
            print("[INFO] WhatsApp Web cargado correctamente.")
        except PlaywrightTimeoutError:
            print("[ERROR] Se agotó el tiempo de espera para cargar WhatsApp Web.")
            await self.stop()
            sys.exit(1)
        except Exception as e:
            print(f"[ERROR] Fallo al iniciar navegador: {e}")
            await self.stop()
            sys.exit(1)

    async def stop(self):
        try:
            if self.browser:
                await self.browser.close()
            if self.playwright:
                await self.playwright.stop()
        except Exception as e:
            print(f"[WARNING] Error al cerrar el navegador: {e}")

    async def get_page(self):
        return self.page