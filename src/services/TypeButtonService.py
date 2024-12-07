from src.services.BotWhatsappService import BotWhatsappService

class TypeButtonService():
    def __init__(self, phone: str, message_text: str, idWa: str, fullName: str):
        self.phone = phone
        self.message_text = message_text
        self.idWa = idWa
        self.fullName = fullName

    def processButton(self) -> dict:
        print("processButton")
        response = {}
        self.message_text = self.message_text.lower()
        print("message_text_lower", self.message_text)
        isBudgetFLow = True if "ingreso" or "gasto" in self.message_text else False 
        if isBudgetFLow:
            botWhatsappService = BotWhatsappService(self.phone, self.message_text, self.idWa, self.fullName)
            response = botWhatsappService.sendMessageInputAmount()
        return response