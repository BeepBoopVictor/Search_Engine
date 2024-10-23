from pymongo import MongoClient
from neo4j import GraphDatabase
import ast


def load_from_mongodb(uri, db_name, collection_name) -> dict:
    client = MongoClient(uri)
    db = client[db_name]
    collection = db[collection_name]

    metadata = {}
    for doc in collection.find():
        for book_id, details in doc.items():
            if book_id != '_id':
                metadata[book_id] = {
                    "title": details.get("title"),
                    "author": details.get("author"),
                    "date": details.get("date"),
                    "language": details.get("language")
                }

    client.close()
    return metadata


def load_from_neo4j(uri, user, password) -> dict:
    driver = GraphDatabase.driver(uri, auth=(user, password))

    query = """
    MATCH (f:File)
    RETURN f.name AS code, f.title AS title, f.author AS author, f.date AS date, f.language AS language
    """

    metadata = {}

    with driver.session() as session:
        result = session.run(query)
        for record in result:
            code = record["code"]
            metadata[code] = {
                "title": record["title"],
                "author": record["author"],
                "date": record["date"],
                "language": record["language"]
            }

    driver.close()
    return metadata


def load_from_txt(file_path):
    metadata = {}
    with open(file_path, 'r', errors='ignore') as file:
        for line in file:
            line_data = ast.literal_eval(line.strip())
            metadata.update(line_data)
    return metadata
