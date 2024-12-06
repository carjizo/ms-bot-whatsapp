from templates.WhatsappTemplates import WhatsappTemplates

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

    def sendTemplateWellcome(self, phoneTo: str, templateName: str) -> dict:
        response = {}
        if templateName == "bienvenida":
            payload = WhatsappTemplates.bienvenida.replace("{phoneTo}", phoneTo)

        try:
            res = requests.post(self.urlSendMessage, headers=self.headersSendMessage, data=json.dumps(payload))
            if res.status_code == 200:
                response["isSucces"] = True
                response["message"] = "Mensaje enviado con éxito."
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
    
    def getURLDocument(self, id_document: str):
        url = f"https://graph.facebook.com/v21.0/{id_document}/"
        payload = {}
        headers = {
            'Authorization': f"Bearer {os.getenv('TOKEN_WHATSAPP')}"
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        response_data = json.loads(response.text)

        return  response_data["url"]
    
    def getImagenContent(self, url: str):
        payload = {}
        headers = {
            'Authorization': f"Bearer {os.getenv('TOKEN_WHATSAPP')}"
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        response.content
        return  response.content