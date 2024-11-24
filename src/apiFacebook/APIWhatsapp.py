import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

class APIWhatsapp():
    def __init__(self):
        self.url = f"https://graph.facebook.com/v21.0/{os.getenv("ID_PHONE_WHATSAPP_BUSINESS")}/messages"
        self.headers = {
            "Authorization": f"Bearer {os.getenv("TOKEN_WHATSAPP")}",
            "Content-Type": "application/json"
        }

    def sendMessageWhatsapp(self, phoneTo: str) -> dict:
        response = {}
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
            res = requests.post(self.url, headers=self.headers, data=json.dumps(payload))
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