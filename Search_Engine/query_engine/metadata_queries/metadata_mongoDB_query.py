import re
from pymongo import MongoClient
from typing import List

# MongoDB connection setup (Assuming MongoDB is running locally on the default port)
client = MongoClient('mongodb://localhost:27017/')
db = client['book_search_engine']  # Replace with your database name
collection = db['metadata_index']   # Replace with your collection name


def search_by_author(author: str) -> List[dict]:
    # Querying MongoDB for documents where the author matches
    results = []
    for doc in collection.find():
        keys = list(doc.keys())
        value = doc[keys[1]]["author"]
        if value == author:
            results.append(doc[keys[1]])
    return results

def search_by_date(date: str) -> List[dict]:
    # Querying MongoDB for documents where the author matches
    results = []
    for doc in collection.find():
        keys = list(doc.keys())
        value = doc[keys[1]]["date"]
        if value == date:
            results.append(doc[keys[1]])
    return results

def search_by_language(language: str) -> List[dict]:
    # Querying MongoDB for documents where the language matches
    results = []
    for doc in collection.find():
        keys = list(doc.keys())
        value = doc[keys[1]]["language"]
        if value == language:
            results.append(doc[keys[1]])
    return results