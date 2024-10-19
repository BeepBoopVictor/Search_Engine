from neo4j import GraphDatabase
import re
from typing import List

# Neo4j connection setup
uri = "neo4j://localhost:7687"  # Replace with your actual URI
username = "neo4j"  # Replace with your username
password = "password"  # Replace with your password

driver = GraphDatabase.driver(uri, auth=(username, password))

def search_by_author(author: str) -> List[dict]:
    query = """
    MATCH (doc:File {author: $author})
    RETURN doc
    """
    with driver.session(database="metadata") as session:
        result = session.run(query, author=author)
        return [record["doc"] for record in result]

def search_by_date(date: str) -> List[dict]:
    query = """
    MATCH (doc:File {date: $date})
    RETURN doc
    """
    with driver.session(database="metadata") as session:
        result = session.run(query, date=date)
        return [record["doc"] for record in result]


def search_by_language(language: str) -> List[dict]:
    query = """
    MATCH (doc:File {language: $language})
    RETURN doc
    """
    with driver.session(database="metadata") as session:
        result = session.run(query, language=language)
        return [record["doc"] for record in result]

