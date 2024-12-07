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

# Crear un nuevo item
@app.post("/items/")
def create_item(item: Item):
    try:
        if not item.id:
            raise HTTPException(status_code=400, detail="El campo 'id' es obligatorio.")
        
        existing_item = db.child("items").child(item.id).get()
        if existing_item.val():
            raise HTTPException(status_code=400, detail="El ID ya existe.")
        
        new_item = item.dict()
        item_id = new_item.pop("id")  # Extrae el ID personalizado
        db.child("items").child(item_id).set(new_item)  # Usa 'set' con el ID especificado
        return {"id": item_id, "message": "Item creado exitosamente."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Leer todos los items
@app.get("/items/")
def read_items():
    try:
        items = db.child("items").get()
        return {"items": items.val() or {}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Leer un item por ID
@app.get("/items/{item_id}")
def read_item(item_id: str):
    try:
        item = db.child("items").child(item_id).get()
        if item.val() is None:
            raise HTTPException(status_code=404, detail="Item no encontrado")
        return {"id": item_id, "item": item.val()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Actualizar un item por ID
@app.put("/items/{item_id}")
def update_item(item_id: str, item: Item):
    try:
        existing_item = db.child("items").child(item_id).get()
        if existing_item.val() is None:
            raise HTTPException(status_code=404, detail="Item no encontrado")

        updated_item = item.dict(exclude_unset=True)  # Solo actualiza los campos enviados
        db.child("items").child(item_id).update(updated_item)
        return {"id": item_id, "message": "Item actualizado exitosamente."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Eliminar un item por ID
@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    try:
        existing_item = db.child("items").child(item_id).get()
        if existing_item.val() is None:
            raise HTTPException(status_code=404, detail="Item no encontrado")

        db.child("items").child(item_id).remove()
        return {"id": item_id, "message": "Item eliminado exitosamente."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))