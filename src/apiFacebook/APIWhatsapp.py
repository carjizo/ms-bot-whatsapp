from src.templates.WhatsappTemplates import WhatsappTemplates

import copy
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

class APIWhatsapp():
    def __init__(self):
        self.urlSendMessage = f"https://graph.facebook.com/v21.0/{os.getenv('ID_PHONE_WHATSAPP_BUSINESS')}/messages"
        self.headersSendMessage = {
            "Authorization": f"Bearer {os.getenv('TOKEN_WHATSAPP')}",
            "Content-Type": "application/json"
        }

    def sendTemplateWellcome(self, phoneTo: str, templateName: str, fullName: str) -> dict:
        if templateName == "bienvenida":
            print("sendTemplateWellcome")
            # template = WhatsappTemplates.bienvenida
            template = copy.deepcopy(WhatsappTemplates.bienvenida)
            template["to"] = template["to"].replace("{phoneTo}",phoneTo)
            template["template"]["components"][1]["parameters"][0]["text"] = template["template"]["components"][1]["parameters"][0]["text"].replace("{userName}", fullName)
            self.payload = template
            self.sendMessage()
    
    def sendTemplateBudgetSummary(self, phoneTo: str, budget: list) -> dict:
        print("sendTemplateBudgetSummary")
        # template = WhatsappTemplates.resumen_presupuesto
        template = copy.deepcopy(WhatsappTemplates.resumen_presupuesto)
        template["to"] = template["to"].replace("{phoneTo}",phoneTo)
        if len(budget) == 3:
            template["template"]["components"][0]["parameters"][0]["text"] = template["template"]["components"][0]["parameters"][0]["text"].replace("{ultimoPeriodo}", budget[0]["periodo"])
            template["template"]["components"][0]["parameters"][1]["text"] = template["template"]["components"][0]["parameters"][1]["text"].replace("{infoaditionalUltimoPeriodo}", budget[0]["aditional"])
            template["template"]["components"][0]["parameters"][2]["text"] = template["template"]["components"][0]["parameters"][2]["text"].replace("{penultimoPeriodo}", budget[1]["periodo"])
            template["template"]["components"][0]["parameters"][3]["text"] = template["template"]["components"][0]["parameters"][3]["text"].replace("{infoaditionalPenultimoPeriodo}", budget[1]["aditional"])
            template["template"]["components"][0]["parameters"][4]["text"] = template["template"]["components"][0]["parameters"][4]["text"].replace("{antepenultimoPeriodo}", budget[2]["periodo"])
            template["template"]["components"][0]["parameters"][5]["text"] = template["template"]["components"][0]["parameters"][5]["text"].replace("{infoaditionalAntepenultimoPeriodo}", budget[2]["aditional"])
        if len(budget) == 2:
            template["template"]["components"][0]["parameters"][0]["text"] = template["template"]["components"][0]["parameters"][0]["text"].replace("{ultimoPeriodo}", budget[0]["periodo"])
            template["template"]["components"][0]["parameters"][1]["text"] = template["template"]["components"][0]["parameters"][1]["text"].replace("{infoaditionalUltimoPeriodo}", budget[0]["aditional"])
            template["template"]["components"][0]["parameters"][2]["text"] = template["template"]["components"][0]["parameters"][2]["text"].replace("{penultimoPeriodo}", budget[1]["periodo"])
            template["template"]["components"][0]["parameters"][3]["text"] = template["template"]["components"][0]["parameters"][3]["text"].replace("{infoaditionalPenultimoPeriodo}", budget[1]["aditional"])
            template["template"]["components"][0]["parameters"][4]["text"] = template["template"]["components"][0]["parameters"][4]["text"].replace("{antepenultimoPeriodo}", " ")
            template["template"]["components"][0]["parameters"][5]["text"] = template["template"]["components"][0]["parameters"][5]["text"].replace("{infoaditionalAntepenultimoPeriodo}", " ")
        if len(budget) == 1:
            template["template"]["components"][0]["parameters"][0]["text"] = template["template"]["components"][0]["parameters"][0]["text"].replace("{ultimoPeriodo}", budget[0]["periodo"])
            template["template"]["components"][0]["parameters"][1]["text"] = template["template"]["components"][0]["parameters"][1]["text"].replace("{infoaditionalUltimoPeriodo}", budget[0]["aditional"])
            template["template"]["components"][0]["parameters"][2]["text"] = template["template"]["components"][0]["parameters"][2]["text"].replace("{penultimoPeriodo}", " ")
            template["template"]["components"][0]["parameters"][3]["text"] = template["template"]["components"][0]["parameters"][3]["text"].replace("{infoaditionalPenultimoPeriodo}", " ")
            template["template"]["components"][0]["parameters"][4]["text"] = template["template"]["components"][0]["parameters"][4]["text"].replace("{antepenultimoPeriodo}", " ")
            template["template"]["components"][0]["parameters"][5]["text"] = template["template"]["components"][0]["parameters"][5]["text"].replace("{infoaditionalAntepenultimoPeriodo}", " ")
        self.payload = template
        self.sendMessage()

    def sendMessageInputAmount(self, phoneTo: str) -> dict:
        print("sendMessageInputAmount")
        # template = WhatsappTemplates.ingresa_monto
        template = copy.deepcopy(WhatsappTemplates.ingresa_monto)
        template["to"] = template["to"].replace("{phoneTo}",phoneTo)
        self.payload = template
        self.sendMessage()
    
    def sendMessage(self):
        print("sendMessage")
        response: dict = {}
        try:
            print(self.urlSendMessage , self.headersSendMessage, self.payload)
            res = requests.post(url=self.urlSendMessage, headers=self.headersSendMessage, data=json.dumps(self.payload))
            if res.status_code == 200:
                response["isSucces"] = True
                response["message"] = "Mensaje enviado con éxito."
                print(response)
                # response["response"] = {}
            else:
                response["isSucces"] = False
                response["message"] = "Error al enviar el mensaje."
                print(f"Error al enviar el mensaje. Código de estado: {res.status_code}")
                print("Detalle:", res.text)
        except requests.exceptions.RequestException as e:
            response["isSucces"] = False
            response["message"] = "Error al enviar el mensaje."
            print(f"Error en la solicitud: {e}")
        
        return response
    
    # def getURLDocument(self, id_document: str):
    #     url = f"https://graph.facebook.com/v21.0/{id_document}/"
    #     payload = {}
    #     headers = {
    #         'Authorization': f"Bearer {os.getenv('TOKEN_WHATSAPP')}"
    #     }
    #     response = requests.request("GET", url, headers=headers, data=payload)
    #     response_data = json.loads(response.text)

    #     return  response_data["url"]
    
    # def getImagenContent(self, url: str):
    #     payload = {}
    #     headers = {
    #         'Authorization': f"Bearer {os.getenv('TOKEN_WHATSAPP')}"
    #     }
    #     response = requests.request("GET", url, headers=headers, data=payload)
    #     response.content
    #     return  response.content