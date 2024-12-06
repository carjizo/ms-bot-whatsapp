from src.services.BotWhatsappService import BotWhatsappService
from src.apiFacebook.APIWhatsapp import APIWhatsapp

class TypeTextService():
    def processText(phone: str, message_text: str) -> dict:
        response = {}
        message_text = message_text.lower()
        isMessageWellcome = True if "hola" in message_text else False 
        if isMessageWellcome:
            botWhatsappService = BotWhatsappService()
            response = botWhatsappService.sendTemplateWellcome(phone, "bienvenida")
        return response