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
        chat = Chat()
        chat.id = self.phoneTo
        chat.lastMessageSend = "template_bienvenida"
        chat.lastMessageReceived = self.message
        firebaseRepository.saveOrUpdate(chat)
    
    def sendMessageInputAmount(self):
        apiWhatsapp.sendMessageInputAmount(self.phoneTo)
        chat = Chat()
        chat.id = self.phoneTo
        chat.lastMessageSend = "template_ingresa_monto"
        chat.lastMessageReceived = self.message
        firebaseRepository.saveOrUpdate(chat)
    
    def processMessage(self):
        item = firebaseRepository.getItem(self.phoneTo)
        chat = Chat(id=self.phoneTo, **item)
        if chat.lastMessageReceived == "ingreso":
            print("Se guardo el monto de ingreso: ", chat)
        if chat.lastMessageReceived == "gasto":
            print("Se guardo el monto de gasto: ", chat)
