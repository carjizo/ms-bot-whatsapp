from src.firebase.Configuration import InitializeFirebase

class FirebaseRepository():
    def __init__(self):
        pass

    def saveOrUpdate(self, item):
        print("saveOrUpdateFirebase")
        print("item")
        try:
            item_data = item.dict()
            print("item_data", item_data)
            item_id = item_data.pop("id")
            print("item_id", item_id)
            InitializeFirebase.db.child("items").child(item_id).set(item_data)
            return {"id": item_id, "message": "Item guardado o actualizado exitosamente."}
        except Exception as e:
            raise Exception(str(e))
        
    def getItem(self, item_id: str):
        print("getItem")
        try:
            item = InitializeFirebase.db.child("items").child(item_id).get()
            if item.val() is None:
                raise Exception("Item no encontrado")
            print("item", item, "item_val", item.val(), "aux", item.id)
            return item
        except Exception as e:
            raise Exception(str(e))