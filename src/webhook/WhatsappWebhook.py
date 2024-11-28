from src.core.ProcessData import ProcessData

import os
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.encoders import jsonable_encoder
from dotenv import load_dotenv

load_dotenv()

class WhatsappWebhook():

    whatsappWebhook = APIRouter()

    @whatsappWebhook.api_route("/webhook/", methods=["POST", "GET"], tags=['bot-whatsapp'])
    async def webhook_whatsapp(request: Request):
        print("request", request)
        if request.method == "GET":
            params = request.query_params
            if params.get('hub.verify_token') == os.getenv('VERIFY_TOKEN_WEBHOOK'):
                return PlainTextResponse(params.get('hub.challenge'))
            else:
                raise HTTPException(status_code=403, detail="Error de autentificación.")

        # Solicitud POST
        data = await request.json()
        try:
            print("data", data)
            info = ProcessData.getData()
            print("info", info)
            return JSONResponse(status_code=200, content=jsonable_encoder("mensaje"))
        except KeyError as e:
            raise JSONResponse(status_code=400, detail=f"Datos incompletos: {e}")