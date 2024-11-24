from pydantic import BaseModel, Field

class RequestSendMessageDTO(BaseModel):
    phoneTo: str = Field(min_length=5, max_length=50)
    message: str = Field(max_length=150)
    
    class Config:
        schema_extra = {
            "example": {
                "phoneTo": "xxxxxxxxxxx",
                "message": "Hola, es un mensaje de prueba"
            }
        }
