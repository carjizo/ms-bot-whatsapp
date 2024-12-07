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
        self.message_text = self.message_text.lower()
        isMessageWellcome = True if "hola" in self.message_text else False
        if isMessageWellcome:
            botWhatsappService = BotWhatsappService(self.phone, "bienvenida", self.idWa, self.fullName)
            response = botWhatsappService.sendTemplateWellcome()
        botWhatsappService = BotWhatsappService(self.phone, self.message_text, self.idWa, self.fullName)
        botWhatsappService.processMessage()
        return response