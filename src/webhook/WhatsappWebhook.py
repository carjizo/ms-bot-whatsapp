from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

class WhatsappWebhook():

    whatsappWebhook = APIRouter()

    @whatsappWebhook.get('/webhook/{args}', tags=['bot-whatsapp'], response_model=dict, status_code=200)
    def sendMessage(args):
        print("args: ")
        print(type(args))
        print(args)
        """
        Send Message to whatsapp\n
        parameter phoneTo\n
        parameter message
        """
        # botWhatsappService.sendMessageWhatsapp(phoneTo)
        return JSONResponse(status_code=200, content=jsonable_encoder("Hello"))


