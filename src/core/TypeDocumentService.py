from src.core.Constants import Constants

class TypeDocumentService():
    def processDocument(mime_type: str, id_document: str) -> dict:
        response = {}
        _type = mime_type.split("/")[1]
        if _type in Constants.MIME_TYPE_IMAGES:
            print("id_document", id_document)
        return response