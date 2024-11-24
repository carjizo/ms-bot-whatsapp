from fastapi import APIRouter
from fastapi import FastAPI, Request, HTTPException
# from fastapi.responses import JSONResponse
# from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, PlainTextResponse

VERIFY_TOKEN = "HolaNovato"

class WhatsappWebhook():

    whatsappWebhook = APIRouter()

    @whatsappWebhook.api_route("/webhook/", methods=["POST", "GET"])
    async def webhook_whatsapp(request: Request):
        # SI HAY DATOS RECIBIDOS VIA GET
        print("request", request)
        if request.method == "GET":
            params = request.query_params
            # SI EL TOKEN ES IGUAL AL QUE RECIBIMOS
            if params.get('hub.verify_token') == "HolaNovato":
                # ESCRIBIMOS EN EL NAVEGADOR EL VALOR DEL RETO RECIBIDO DESDE FACEBOOK
                return PlainTextResponse(params.get('hub.challenge'))
            else:
                # SI NO SON IGUALES RETORNAMOS UN MENSAJE DE ERROR
                raise HTTPException(status_code=403, detail="Error de autentificación.")

        # SI LA PETICIÓN ES POST, RECIBIMOS LOS DATOS ENVIADOS VIA JSON
        data = await request.json()
        try:
            # EXTRAEMOS EL NÚMERO DE TELÉFONO Y EL MENSAJE
            telefono = data['entry'][0]['changes'][0]['value']['messages'][0]['from']
            mensaje_texto = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
            mensaje = f"Telefono: {telefono} | Mensaje: {mensaje_texto}"
            print("mensaje: ", mensaje)
            # ESCRIBIMOS EL NÚMERO DE TELÉFONO Y EL MENSAJE EN EL ARCHIVO TEXTO
            # with open("texto.txt", "w") as f:
            #     f.write(mensaje)

            # RETORNAMOS EL STATUS EN UN JSON
            return JSONResponse(content={"status": "success"}, status_code=200)
        except KeyError as e:
            raise HTTPException(status_code=400, detail=f"Datos incompletos: {e}")