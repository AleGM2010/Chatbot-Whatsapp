
from bot_whatsapp.interfaces import IMessageCache




class DefaultMessageCache(IMessageCache):
    def __init__(self):
        self.cache = set()

    def add_message(self, message_key):
        self.cache.add(message_key)

    def is_message_processed(self, message_key):
        return message_key in self.cache