from pymongo import MongoClient

def setup_books(count):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["book_search_engine"]
    collection = db["books"] 

    collection.delete_many({})

    for i in range(count):
        book = {
            "title": f"Book {i + 1}",
            "content": f"Este es el contenido del libro {i + 1}. Contiene texto sobre la libertad y los derechos. democracy"
        }
        collection.insert_one(book)
