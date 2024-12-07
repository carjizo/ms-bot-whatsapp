from src.services.BotWhatsappService import BotWhatsappService

class TypeTextService():
    def processText(phone: str, message_text: str) -> dict:
        print("processText")
        response = {}
        message_text = message_text.lower()
        print("message_text_lower", message_text)
        isMessageWellcome = True if "hola" in message_text else False
        if isMessageWellcome:
            botWhatsappService = BotWhatsappService(phone, "bienvenida")
            response = botWhatsappService.sendTemplateWellcome()
        botWhatsappService = BotWhatsappService(phone, message_text)
        botWhatsappService.processMessage()
        return response