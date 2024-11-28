from src.core.Constants import Constants

class ProcessData():
    def getData(data: dict) -> dict:
        response = {}
        print("self.data", data, type(data))
        phone = data['entry'][0]['changes'][0]['value']['messages'][0]['from']
        type = data['entry'][0]['changes'][0]['value']['messages'][0]
        response["phone"] = phone
        response["type"] = type
        if type == Constants.TYPE_TEXT:
            message_text = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
            response["message_text"] = message_text
        if type == Constants.TYPE_DOCUMENT:
            mime_type = data['entry'][0]['changes'][0]['value']['messages'][0]['document']['mime_type']
            id_document = data['entry'][0]['changes'][0]['value']['messages'][0]['document']['id']
            response["mime_type"] = mime_type
            response["id_document"] = id_document
        
        return response