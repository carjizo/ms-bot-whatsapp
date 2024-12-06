from src.dtos.RequestSendMessageDTO import RequestSendMessageDTO
from src.services.BotWhatsappService import BotWhatsappService

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

botWhatsappService = BotWhatsappService()

class BotWhatsappController():

    botWhatsappController = APIRouter()

    @botWhatsappController.post('/send-message', tags=['bot-whatsapp'], response_model=dict, status_code=200)
    def sendMessage(requestSendMessage: RequestSendMessageDTO):
        """
        Send Message to whatsapp\n
        parameter phoneTo\n
        parameter message
        """
        phoneTo: str =  requestSendMessage.phoneTo
        print("phoneTo", phoneTo)
        # botWhatsappService.sendMessageWhatsapp(phoneTo)
        return JSONResponse(status_code=200, content=jsonable_encoder("Hello"))
