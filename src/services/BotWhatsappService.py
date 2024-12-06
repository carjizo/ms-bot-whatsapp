from src.apiFacebook.APIWhatsapp import APIWhatsapp

apiWhatsapp = APIWhatsapp()

class BotWhatsappService():
    def __init__(self):
        pass

    def sendTemplateWellcome(self, phoneTo: str, message: str):
        apiWhatsapp.sendTemplateWellcome(phoneTo, message)