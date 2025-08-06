from abc import ABC, abstractmethod

# Interfaces (Clases abstractas)
class IBrowserManager(ABC):
    @abstractmethod
    async def start(self):
        pass

    @abstractmethod
    async def stop(self):
        pass

    @abstractmethod
    async def get_page(self):
        pass

class IWhatsAppInterface(ABC):
    @abstractmethod
    async def initialize(self, page):
        pass

    @abstractmethod
    async def send_message(self, text):
        pass

    @abstractmethod
    async def wait_for_user_click(self, message):
        pass

    @abstractmethod
    async def get_new_messages(self, start_time):
        pass

    @abstractmethod
    async def show_initial_message(self):
        pass

class IResponseLogic(ABC):
    @abstractmethod
    def get_response(self, message):
        pass

class IMessageCache(ABC):
    @abstractmethod
    def add_message(self, message_key):
        pass

    @abstractmethod
    def is_message_processed(self, message_key):
        pass
