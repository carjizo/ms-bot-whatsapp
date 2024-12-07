from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pyrebase
import firebase_admin
from firebase_admin import credentials,auth
from dotenv import load_dotenv
import os

load_dotenv()


if not firebase_admin._apps:
    # cred = credentials.Certificate("realtimechat-firebase-adminsdk.json")
    cred = credentials.Certificate({
        "type": os.getenv("FIREBASE_TYPE"),
        "project_id": os.getenv("FIREBASE_PROJECT_ID"),
        "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
        "private_key": os.getenv("FIREBASE_PRIVATE_KEY").replace("\\n", "\n"),  # Manejo de saltos de línea
        "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
        "client_id": os.getenv("FIREBASE_CLIENT_ID"),
        "auth_uri": os.getenv("FIREBASE_AUTH_URI"),
        "token_uri": os.getenv("FIREBASE_TOKEN_URI"),
        "auth_provider_x509_cert_url": os.getenv("FIREBASE_AUTH_PROVIDER_CERT_URL"),
        "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_CERT_URL"),
        "universe_domain": os.getenv("FIREBASE_UNIVERSE_DOMAIN")
    })
    firebase_admin.initialize_app(cred)

# Configuración de Firebase
firebase_config = {
    "apiKey": os.getenv("FIREBASE_TYPE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
    "measurementId": os.getenv("FIREBASE_MEASUREMENT_ID")
}

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()

# Inicializa FastAPI
app = FastAPI()

# Modelo de datos
class Item(BaseModel):
    id: str = None  # Opcional, para especificar un ID
    name: str
    description: str = None
    price: float

@app.post("/items/")
def save_or_update_item(item: Item):
    try:
        item_data = item.dict()
        item_id = item_data.pop("id")

        # `set` sobrescribirá o creará los datos en Firebase
        db.child("items").child(item_id).set(item_data)
        return {"id": item_id, "message": "Item guardado o actualizado exitosamente."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))