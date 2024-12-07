from src.services.BotWhatsappService import BotWhatsappService

class TypeTextService():
    def __init__(self, phone: str, message_text: str, idWa: str, fullName: str):
        self.phone = phone
        self.message_text = message_text
        self.idWa = idWa
        self.fullName = fullName

    def processText(self) -> dict:
        print("processText")
        response = {}
        message_text = message_text.lower()
        isMessageWellcome = True if "hola" in message_text else False
        if isMessageWellcome:
            botWhatsappService = BotWhatsappService(self.phone, "bienvenida", self.idWa, self.fullName)
            response = botWhatsappService.sendTemplateWellcome()
        botWhatsappService = BotWhatsappService(self.phone, message_text, self.idWa, self.fullName)
        botWhatsappService.processMessage()
        return response