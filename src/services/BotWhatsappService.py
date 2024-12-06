from src.apiFacebook.APIWhatsapp import APIWhatsapp

apiWhatsapp = APIWhatsapp()

class BotWhatsappService():
    def __init__(self):
        pass

    def sendTemplateWellcome(self, phoneTo: str, message: str):
        apiWhatsapp.sendTemplateWellcome(phoneTo, message)
    
    def sendMessageInputAmount(self, phoneTo: str):
        apiWhatsapp.sendMessageInputAmount(phoneTo)