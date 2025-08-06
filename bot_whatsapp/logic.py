
from bot_whatsapp.interfaces import IResponseLogic


class DefaultResponseLogic(IResponseLogic):
    def __init__(self):
        self.respuestas = {
            "hola": "¡Hola! ¿Cómo estás?",
            "precio": "Los precios varían según el producto. ¿Podés especificar cuál te interesa?",
            "gracias": "¡De nada! 😊",
            "adios": "¡Hasta luego!",
            "quien sos": "Soy un bot de atención automática. ¿En qué puedo ayudarte?",
            "Hola": "¡Hola! ¿Cómo estás?",
            "Precio": "Los precios varían según el producto. ¿Podés especificar cuál te interesa?",
            "Gracias": "¡De nada! 😊",
            "Adiós": "¡Hasta luego!",
            "Quien sos?": "Soy un bot de atención automática. ¿En qué puedo ayudarte?"
        }

    def get_response(self, message):
        message = message.lower().strip()
        for clave in self.respuestas:
            if clave in message:
                return self.respuestas[clave]
        return "Lo siento, no entendí tu mensaje. ¿Podés repetirlo de otra forma?"