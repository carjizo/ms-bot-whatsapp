from src.constants.Constants import Constants
from src.apiFacebook.APIWhatsapp import APIWhatsapp

class TypeDocumentService():
    def processDocument(mime_type: str, id_document: str) -> dict:
        response = {}
        _type = mime_type.split("/")[1]
        if _type in Constants.MIME_TYPE_IMAGES:
            apiWhatsapp = APIWhatsapp()
            url = apiWhatsapp.getURLDocument(id_document)
            image_content = apiWhatsapp.getImagenContent(url)
        return response