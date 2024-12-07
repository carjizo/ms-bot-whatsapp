from src.firebase.Configuration import InitializeFirebase

class FirebaseRepository():
    def __init__(self):
        pass

    def saveOrUpdate(self, item):
        print("saveOrUpdateFirebase")
        try:
            item_data = item.dict()
            item_id = item_data.pop("id")
            InitializeFirebase.db.child("items").child(item_id).set(item_data)
            return {"id": item_id, "message": "Item guardado o actualizado exitosamente."}
        except Exception as e:
            raise Exception(str(e))
        
    def getItem(self, item_id: str):
        print("getItem")
        try:
            item = InitializeFirebase.db.child("items").child(item_id).get()
            data = item.val()
            if not data:
                raise Exception("Item no encontrado")
            data = dict(data)
            return data
        except Exception as e:
            raise Exception(str(e))