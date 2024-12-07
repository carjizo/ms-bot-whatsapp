from src.services.BotWhatsappService import BotWhatsappService

class TypeButtonService():
    def processButton(phone: str, message_text: str) -> dict:
        print("processButton")
        response = {}
        message_text = message_text.lower()
        print("message_text_lower", message_text)
        isBudgetFLow = True if "ingreso" or "gasto" in message_text else False 
        if isBudgetFLow:
            botWhatsappService = BotWhatsappService(phone, message_text)
            response = botWhatsappService.sendMessageInputAmount()
        return response