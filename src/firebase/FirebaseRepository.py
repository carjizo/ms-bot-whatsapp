from src.firebase.Configuration import InitializeFirebase

class FirebaseRepository:
    def saveOrUpdate(item):
        try:
            item_data = item.dict()
            item_id = item_data.pop("id")
            InitializeFirebase.db.child("items").child(item_id).set(item_data)
            return {"id": item_id, "message": "Item guardado o actualizado exitosamente."}
        except Exception as e:
            raise Exception(str(e))
        
    def getItem(item_id: str):
        try:
            item = InitializeFirebase.db.child("items").child(item_id).get()
            if item.val() is None:
                raise Exception("Item no encontrado")
            print("item", item, "item_val", item.val())
            return item.val()
        except Exception as e:
            raise Exception(str(e))