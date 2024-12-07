from src.apiFacebook.APIWhatsapp import APIWhatsapp
from src.firebase.FirebaseRepository import FirebaseRepository
from src.models.Chat import Chat

from datetime import datetime

apiWhatsapp = APIWhatsapp()
firebaseRepository = FirebaseRepository()

class BotWhatsappService():
    def __init__(self, phoneTo: str, message: str):
        self.phoneTo = phoneTo
        self.message = message
        fecha_actual = datetime.now()
        self.year = fecha_actual.strftime("%Y")
        self.month = fecha_actual.strftime("%m")
        self.day = fecha_actual.strftime("%d")

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
            firebaseRepository.saveOrUpdateHistory({
                self.phoneTo: {
                    self.year: {
                        self.month: {
                            self.day: {
                                "ingreso": self.message,
                                "gasto": None
                            }
                        }
                    }
                }
            })                
        if chat.lastMessageReceived == "gasto":
            print("Se guardo el monto de gasto: ", chat)
            firebaseRepository.saveOrUpdateHistory({
                self.phoneTo: {
                    self.year: {
                        self.month: {
                            self.day: {
                                "ingreso": None,
                                "gasto": self.message
                            }
                        }
                    }
                }
            }) 
