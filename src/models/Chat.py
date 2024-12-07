from pydantic import BaseModel
from typing import Optional

class Chat(BaseModel):
    id: str
    lastMessageSend: Optional[str] = None
    lastMessageReceived: Optional[str] = None
    fullName: Optional[str] = None
    idWa: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "id": "51999999999",
                "lastMessageSend": "last message sent",
                "lastMessageReceived": "last message received",
                "fullName": "usuario test",
                "idWa": "4353246234"
            }
        }