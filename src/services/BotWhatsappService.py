from apiFacebook.APIWhatsapp import APIWhatsapp

apiWhatsapp = APIWhatsapp()

class BotWhatsappService():
    def __init__(self):
        pass

    def sendMessageWhatsapp(self, phoneTo: str):
        apiWhatsapp.sendMessageWhatsapp(phoneTo)