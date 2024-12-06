from constants.Constants import Constants
from src.services.TypeDocumentService import TypeDocumentService
from src.services.TypeTextServiceService import TypeTextService

class ProcessData():
    def processData(data: dict) -> dict:
        response = {}
        dataMessage = data['entry'][0]['changes'][0]['value']['messages'][0]
        phone = dataMessage['from']
        type_event = dataMessage['type']
        
        response["phone"] = phone
        response["type"] = type_event
        
        if type_event == Constants.TYPE_TEXT:
            message_text = dataMessage['text']['body']
            response["message_text"] = message_text
            TypeTextService.processText(phone, message_text)
        elif type_event == Constants.TYPE_DOCUMENT:
            mime_type = dataMessage['document']['mime_type']
            id_document = dataMessage['document']['id']
            response["mime_type"] = mime_type
            response["id_document"] = id_document
        elif type_event == Constants.TYPE_IMAGE:
            mime_type = dataMessage['image']['mime_type']
            id_document = dataMessage['image']['id']
            response["mime_type"] = mime_type
            response["id_document"] = id_document
            TypeDocumentService.processDocument(mime_type, id_document)
        
        return response