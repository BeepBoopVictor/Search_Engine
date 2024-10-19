from pymongo import MongoClient

# Connect to mongoDB
client              = MongoClient("mongodb://localhost:27017/")
db                  = client["book_search_engine"]  # Database
metadata_collection = db["metadata_index"]  # Metadata Collection


# Function to store a whole dictionary
def metadata_index_from_mongodb(metadata: dict):

    for key, value in metadata.items():
        if metadata_collection.count_documents({key: {'$exists': True}}) == 0:
            # Si no existe, insertar el documento
            metadata_collection.insert_one({key: value})
            print(f"Inserted: {key}")
        else:
            print(f"Already exists: {key}")
