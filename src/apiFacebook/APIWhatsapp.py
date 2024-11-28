import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

class APIWhatsapp():
    def __init__(self):
        pass

    def sendMessageWhatsapp(self, phoneTo: str) -> dict:
        response = {}
        url = f"https://graph.facebook.com/v21.0/{os.getenv('ID_PHONE_WHATSAPP_BUSINESS')}/messages"
        headers = {
            "Authorization": f"Bearer {os.getenv('TOKEN_WHATSAPP')}",
            "Content-Type": "application/json"
        }
        payload = {
            "messaging_product": "whatsapp",
            "to": phoneTo,
            "type": "template",
            "template": {
                "name": "message_dev",
                "language": {
                    "code": "es_MX"
                }
            }
        }

        try:
            res = requests.post(url, headers=headers, data=json.dumps(payload))
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