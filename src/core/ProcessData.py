from src.core.Constants import Constants
from src.core.TypeDocumentService import TypeDocumentService

class ProcessData():
    def processData(data: dict) -> dict:
        response = {}
        phone = data['entry'][0]['changes'][0]['value']['messages'][0]['from']
        type_event = data['entry'][0]['changes'][0]['value']['messages'][0]['type']
        response["phone"] = phone
        response["type"] = type_event
        if type_event == Constants.TYPE_TEXT:
            message_text = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
            response["message_text"] = message_text
        if type_event == Constants.TYPE_DOCUMENT:
            mime_type = data['entry'][0]['changes'][0]['value']['messages'][0]['document']['mime_type']
            id_document = data['entry'][0]['changes'][0]['value']['messages'][0]['document']['id']
            response["mime_type"] = mime_type
            response["id_document"] = id_document
        if type_event == Constants.TYPE_IMAGE:
            mime_type = data['entry'][0]['changes'][0]['value']['messages'][0]['image']['mime_type']
            id_document = data['entry'][0]['changes'][0]['value']['messages'][0]['image']['id']
            response["mime_type"] = mime_type
            response["id_document"] = id_document
            TypeDocumentService.processDocument(mime_type, id_document)
        
        return response