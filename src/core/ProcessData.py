from core.Constants import Constants

class ProcessData():
    def __init__(self, data: dict):
        self.data = data
    
    def getData(self) -> dict:
        response = {}
        phone = self.data['entry'][0]['changes'][0]['value']['messages'][0]['from']
        type = self.data['entry'][0]['changes'][0]['value']['messages'][0]
        response["phone"] = phone
        response["type"] = type
        if type == Constants.TYPE_TEXT:
            message_text = self.data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
            response["message_text"] = message_text
        if type == Constants.TYPE_DOCUMENT:
            mime_type = self.data['entry'][0]['changes'][0]['value']['messages'][0]['document']['mime_type']
            id_document = self.data['entry'][0]['changes'][0]['value']['messages'][0]['document']['id']
            response["mime_type"] = mime_type
            response["id_document"] = id_document
        
        return response