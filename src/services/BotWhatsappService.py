from src.apiFacebook.APIWhatsapp import APIWhatsapp
from src.firebase.FirebaseRepository import FirebaseRepository
from src.models.Chat import Chat
from src.constants.Constants import Constants

from datetime import datetime

apiWhatsapp = APIWhatsapp()
firebaseRepository = FirebaseRepository()

class BotWhatsappService():
    def __init__(self, phoneTo: str, message: str, idWa: str, fullName: str):
        self.phoneTo = phoneTo
        self.message = message
        self.idWa = idWa
        self.fullName = fullName
        fecha_actual = datetime.now()
        self.year = fecha_actual.strftime("%Y")
        self.month = fecha_actual.strftime("%m")
        self.day = fecha_actual.strftime("%d")

    def sendTemplateWellcome(self):
        apiWhatsapp.sendTemplateWellcome(self.phoneTo, self.message, self.fullName)
        chat = Chat()
        chat.id = self.phoneTo
        chat.lastMessageSend = "template_bienvenida"
        chat.fullName = self.fullName
        chat.idWa = self.idWa
        chat.lastMessageReceived = self.message
        firebaseRepository.saveOrUpdate(chat)
    
    def sendMessageInputAmount(self):
        apiWhatsapp.sendMessageInputAmount(self.phoneTo)
        chat = Chat()
        chat.id = self.phoneTo
        chat.lastMessageSend = "template_ingresa_monto"
        chat.fullName = self.fullName
        chat.idWa = self.idWa
        chat.lastMessageReceived = self.message
        firebaseRepository.saveOrUpdate(chat)
    
    def processMessage(self):
        item: dict = firebaseRepository.getItem(self.phoneTo)
        chat: Chat = Chat(id=self.phoneTo, **item)
        if chat.lastMessageReceived in [Constants.BUTTON_REGISTRAR_GASTO, Constants.BUTTON_REGISTRAR_INGRESO]:
            self.budgetFlow(chat)
        chat.id = self.phoneTo
        chat.fullName = self.fullName
        chat.idWa = self.idWa
        chat.lastMessageReceived = self.message
        firebaseRepository.saveOrUpdate(chat)

    def budgetFlow(self, chat: Chat):
        historyItem = firebaseRepository.getItemHistory(self.phoneTo)
        if not historyItem.get(self.year, {}):
            historyItem[self.year] = {}
        if not historyItem[self.year].get(self.month, {}):
            historyItem[self.year][self.month] = {}
        if not historyItem[self.year][self.month].get(self.day, {}):
            historyItem[self.year][self.month][self.day] = {"ingreso": 0, "gasto": 0}

        dayItem = historyItem[self.year][self.month][self.day]
        dayAmountIngreso: float = dayItem["ingreso"] 
        dayAmountGasto: float = dayItem["gasto"]
        if chat.lastMessageReceived == Constants.BUTTON_REGISTRAR_INGRESO:
            dayAmountIngreso = dayAmountIngreso + float(self.message)
            historyItem[self.year][self.month][self.day]["ingreso"] = dayAmountIngreso
            firebaseRepository.saveOrUpdateHistory({"id": self.phoneTo,"data": historyItem})                
        if chat.lastMessageReceived == Constants.BUTTON_REGISTRAR_GASTO:
            dayAmountGasto = dayAmountGasto + float(self.message)
            historyItem[self.year][self.month][self.day]["gasto"] = dayAmountGasto
            firebaseRepository.saveOrUpdateHistory({"id": self.phoneTo,"data": historyItem})  