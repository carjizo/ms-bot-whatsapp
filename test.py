from paddleocr import PaddleOCR

class PaddleOCRModel():
    def __init__(self, img):
        self.img = img

    def getData(self):
        paddle_ocr = PaddleOCR(lang='es')
        paddle_result = paddle_ocr.ocr(self.img, cls=True)
        for rsp in paddle_result:
            # print(rsp)
            for i in rsp:
                print(i)

######################
import requests
import json

url = "https://graph.facebook.com/v21.0/1609581072983618/"

payload = {}
headers = {
    'Authorization': 'Bearer EAAIPr8a3u6UBOz86U1bZBlDZB0eqVPMLDy4zPAk4BU7CKvYNs9yBSJnezMZB9iorrqGZAoyjKszZBP879n0BUeK6sZCyJZCNOahU2CtbVJNttrZAnjwyBZCvdArJEr2nvbZAJM5PMEiZAVphujdCT5QZBpK1lzBihP3PSfXfNXlZClZBVpNLjya95ZAqwzz9kkuhOQDpjbRIwZDZD'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Convierte el texto de respuesta a un diccionario
response_data = json.loads(response.text)
_url = ""
# Accede al campo "url" si existe
if "url" in response_data:
    _url = response_data["url"]
    print(_url)
else:
    print("La clave 'url' no está presente en la respuesta.")


payload = {}
headers = {
    'Authorization': 'Bearer EAAIPr8a3u6UBOz86U1bZBlDZB0eqVPMLDy4zPAk4BU7CKvYNs9yBSJnezMZB9iorrqGZAoyjKszZBP879n0BUeK6sZCyJZCNOahU2CtbVJNttrZAnjwyBZCvdArJEr2nvbZAJM5PMEiZAVphujdCT5QZBpK1lzBihP3PSfXfNXlZClZBVpNLjya95ZAqwzz9kkuhOQDpjbRIwZDZD'
}

image_response = requests.request("GET", _url, headers=headers, data=payload)
image_response.content
# Verifica si la respuesta contiene la imagen
# if image_response.status_code == 200:
#     image_path = r"C:\Users\carlo\Documents\PersonalPojects\ms-bot-whatsapp\imagen.jpg"  # Cambia esto a la ruta deseada
#     with open(image_path, "wb") as image_file:
#         image_file.write(image_response.content)
#     print(f"Imagen guardada en: {image_path}")
# else:
#     print(f"No se pudo descargar la imagen. Código de estado: {image_response.status_code}")

paddle_ocr = PaddleOCRModel(image_response.content)
paddle_ocr.getData()
