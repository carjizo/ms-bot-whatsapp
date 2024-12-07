from src.apiFacebook.APIWhatsapp import APIWhatsapp
from src.firebase.FirebaseRepository import FirebaseRepository
from src.models.Chat import Chat

apiWhatsapp = APIWhatsapp()
firebaseRepository = FirebaseRepository()

class BotWhatsappService():
    def __init__(self, phoneTo: str, message: str):
        self.phoneTo = phoneTo
        self.message = message

    def sendTemplateWellcome(self):
        apiWhatsapp.sendTemplateWellcome(self.phoneTo, self.message)
        Chat.id = self.phoneTo
        Chat.lastMessageSend = "template_bienvenida"
        firebaseRepository.saveOrUpdate(Chat)
    
    def sendMessageInputAmount(self):
        apiWhatsapp.sendMessageInputAmount(self.phoneTo)
        Chat.id = self.phoneTo
        Chat.lastMessageSend = "template_ingresa_monto"
        Chat.lastMessageReceived = self.message
        firebaseRepository.saveOrUpdate(Chat)
    
    def processMessage(self):
        message: Chat = firebaseRepository.getItem(self.phoneTo)
        if message.lastMessageReceived == "ingreso":
            print("Se guardo el monto de ingreso: ", message)
        if message.lastMessageReceived == "gasto":
            print("Se guardo el monto de gasto: ", message)
