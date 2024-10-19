import re
from pymongo import MongoClient
from typing import List

# MongoDB connection setup (Assuming MongoDB is running locally on the default port)
client = MongoClient('mongodb://localhost:27017/')
db = client['book_search_engine']  # Replace with your database name
collection = db['metadata_index']   # Replace with your collection name


def search_by_author(author: str) -> List[dict]:
    # Querying MongoDB for documents where the author matches
    return list(collection.find({"author": author}))


def search_by_date(date: str) -> List[dict]:
    # Querying MongoDB for documents where the date matches
    return list(collection.find({"date": date}))



def search_by_language(language: str) -> List[dict]:
    # Querying MongoDB for documents where the language matches
    return list(collection.find({"language": language}))

