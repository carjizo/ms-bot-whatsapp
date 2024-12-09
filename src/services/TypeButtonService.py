from src.services.BotWhatsappService import BotWhatsappService
from src.constants.Constants import Constants

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
        isBudgetFLow: bool = False
        botWhatsappService = BotWhatsappService(self.phone, self.message_text, self.idWa, self.fullName)
        if (self.message_text in [Constants.BUTTON_REGISTRAR_GASTO, Constants.BUTTON_REGISTRAR_INGRESO]): 
            isBudgetFLow = True
        if isBudgetFLow:
            response = botWhatsappService.sendMessageInputAmount()
        if self.message_text == Constants.BUTTON_RESUMEN_PRESUPUESTO:            
            response = botWhatsappService.sendMessageInputBudgetSummary()
        return response