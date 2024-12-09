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
    
    def sendMessageInputBudgetSummary(self):
        item: dict = firebaseRepository.getItem(self.phoneTo)
        chat: Chat = Chat(id=self.phoneTo, **item)
        self.budgetSummary()
        chat.lastMessageSend = "template_resumen_presupuesto"
        chat.id = self.phoneTo
        chat.fullName = self.fullName
        chat.idWa = self.idWa
        chat.lastMessageReceived = self.message
        firebaseRepository.saveOrUpdate(chat)
    
    def processMessage(self):
        item: dict = firebaseRepository.getItem(self.phoneTo)
        chat: Chat = Chat(id=self.phoneTo, **item)
        if chat.lastMessageReceived in [Constants.BUTTON_REGISTRAR_GASTO, Constants.BUTTON_REGISTRAR_INGRESO]:
            self.saveAmount(chat.lastMessageReceived)
        chat.id = self.phoneTo
        chat.fullName = self.fullName
        chat.idWa = self.idWa
        chat.lastMessageReceived = self.message
        firebaseRepository.saveOrUpdate(chat)

    def budgetSummary(self):
        dayAmountIngreso, dayAmountGasto = self.infoBudget()
        print(self.historyItem)
        keys = sorted(self.historyItem[self.year].keys())
        lastKeys = keys[-3:]
        lastRecords = {key: self.historyItem[self.year][key] for key in lastKeys}
        budget: list = []
        for month, infoMonths in lastRecords.items():
            totalIngreso = 0
            totalGasto = 0
            for infoDays in infoMonths.values():
                totalIngreso += infoDays["ingreso"]
                totalGasto += infoDays["gasto"]
            budget.append({
                "periodo": f"Periodo: {Constants.CALENDARY_SPANISH[month]}",
                "aditional": f"Ingresos: {totalIngreso}, Gastos: {totalGasto}, Resumen: {totalIngreso - totalGasto}"
            })
        apiWhatsapp.sendTemplateBudgetSummary(self.phoneTo, budget)

    def saveAmount(self, lastMessageReceived: str):
        dayAmountIngreso, dayAmountGasto = self.infoBudget()
        if lastMessageReceived == Constants.BUTTON_REGISTRAR_INGRESO:
            dayAmountIngreso = dayAmountIngreso + float(self.message)
            self.historyItem[self.year][self.month][self.day]["ingreso"] = dayAmountIngreso
            firebaseRepository.saveOrUpdateHistory({"id": self.phoneTo,"data": self.historyItem})                
        if lastMessageReceived == Constants.BUTTON_REGISTRAR_GASTO:
            dayAmountGasto = dayAmountGasto + float(self.message)
            self.historyItem[self.year][self.month][self.day]["gasto"] = dayAmountGasto
            firebaseRepository.saveOrUpdateHistory({"id": self.phoneTo,"data": self.historyItem})
    
    def infoBudget(self) -> tuple[float, float]:
        self.historyItem = firebaseRepository.getItemHistory(self.phoneTo)
        if not self.historyItem.get(self.year, {}):
            self.historyItem[self.year] = {}
        if not self.historyItem[self.year].get(self.month, {}):
            self.historyItem[self.year][self.month] = {}
        if not self.historyItem[self.year][self.month].get(self.day, {}):
            self.historyItem[self.year][self.month][self.day] = {"ingreso": 0, "gasto": 0}

        dayItem = self.historyItem[self.year][self.month][self.day]
        dayAmountIngreso: float = dayItem["ingreso"] 
        dayAmountGasto: float = dayItem["gasto"]
        return dayAmountIngreso, dayAmountGasto