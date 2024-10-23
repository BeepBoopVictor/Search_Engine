from pymongo import MongoClient

# Connect to mongoDB
client              = MongoClient("mongodb://localhost:27017/")
db                  = client["book_search_engine"]  # Database
inverted_index      = db["invertedindex"]  # inverted_index Collection



def inverted_index_from_mongodb(inverted_index_dict: dict):
    #inverted_index.delete_many({})
    for word, files in inverted_index_dict.items():
        for file_id, positions in files.items():
            # Updates or inserts the inverted index
            inverted_index.update_one(
                {"word": word},
                {
                    "$addToSet": {f"files.{file_id}": [positions['positions'], positions['count']]}
                },
                upsert=True
            )
