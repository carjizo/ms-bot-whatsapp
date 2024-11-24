from controllers.BotWhatsappController import BotWhatsappController

from fastapi import FastAPI

app = FastAPI()

app.title = "Bot Whatsapp"
app.version = "0.0.1"
app.include_router(BotWhatsappController.botWhatsappController)