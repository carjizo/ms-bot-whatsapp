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
        item: dict = firebaseRepository.getItem(self.phoneTo)
        chat: Chat = Chat(id=self.phoneTo, **item)
        if chat.lastMessageReceived in ["ingreso", "gasto"]:
            self.budgetFlow(chat)
        
    def budgetFlow(self, chat: Chat):
        historyItem = firebaseRepository.getItemHistory(self.phoneTo)
        if not historyItem.get(self.year, {}):
            historyItem[self.year] = {}
        if not historyItem[self.year].get(self.month, {}):
            historyItem[self.year][self.month] = {}
        if not historyItem[self.year][self.month].get(self.day, {}):
            historyItem[self.year][self.month][self.day] = {"ingreso": 0, "gasto": 0}

        dayItem = historyItem[self.year][self.month][self.day]
        print("dayItem", dayItem)
        dayAmountIngreso: float = dayItem["ingreso"] 
        dayAmountGasto: float = dayItem["gasto"]
        if chat.lastMessageReceived == "ingreso":
            dayAmountIngreso = dayAmountIngreso + float(self.message)
            dayItem["ingreso"] = dayAmountIngreso
            print("item_for_save", dayItem)
            firebaseRepository.saveOrUpdateHistory({"id": self.phoneTo,"data": dayItem})                
        if chat.lastMessageReceived == "gasto":
            dayAmountGasto = dayAmountGasto + float(self.message)
            dayItem["gasto"] = dayAmountGasto
            print("item_for_save", dayItem)
            firebaseRepository.saveOrUpdateHistory({"id": self.phoneTo,"data": dayItem})  