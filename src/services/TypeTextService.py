from src.services.BotWhatsappService import BotWhatsappService

class TypeTextService():
    def processText(phone: str, message_text: str) -> dict:
        print("processText")
        response = {}
        message_text = message_text.lower()
        print("message_text_lower", message_text)
        isMessageWellcome = True if "hola" in message_text else False 
        if isMessageWellcome:
            botWhatsappService = BotWhatsappService()
            response = botWhatsappService.sendTemplateWellcome(phone, "bienvenida")
        isAmount = message_text.isnumeric()
        if isAmount:
            print("#1")
            # botWhatsappService = BotWhatsappService()
            # response = botWhatsappService.sendTemplateWellcome(phone, message_text)
        return response