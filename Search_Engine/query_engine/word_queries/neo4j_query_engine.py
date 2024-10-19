import re
from neo4j import GraphDatabase
from nltk.corpus import stopwords
import nltk
from typing import List
from datetime import datetime
import os

DATABASE_URL = 'bolt://localhost:7687' #os.getenv('DATABASE_URL')
DATABASE_USER = "neo4j" #os.getenv('DATABASE_USER')
DATABASE_PASSWORD = "unodostres" #os.getenv('DATABASE_PASSWORD')

driver = GraphDatabase.driver(DATABASE_URL, auth=(DATABASE_USER, DATABASE_PASSWORD))

def close_neo4j():
    driver.close()

def search_word_in_all_documents(word: str):
    """
    Search for a word in all documents.
    """
    word = word.lower()  # Convert the word to lowercase for search
    with driver.session(database="invertedindex") as session:
        result = session.run(
            """
            MATCH (w:Word {word: $word})-[r:APPEARS_IN]->(d:Document)
            RETURN d.title AS document, r.positions AS positions, w.count AS count
            """,
            word=word
        )

        matches = [(record["document"], record["positions"], record["count"]) for record in result]

        if matches:
            return matches
        else:
            return []



def search_word_with_context(word: str, document_folder: str, context_size: int = 30):
    """
    Search for a word and return the context around its occurrences in the documents.
    """
    word = word.lower()
    context = {}
    inverted_index = {}
    contexts = {}
    with driver.session(database="invertedindex") as session:
        result = session.run(
            """
            MATCH (w:Word {word: $word})-[r:APPEARS_IN]->(d:Document)
            RETURN d.title AS document, d.title AS content, r.positions AS positions
            """,
            word=word
        )

        for record in result:
            document = record["document"]
            content = record["content"]
            positions = record["positions"]

            for pos in positions:
                start = max(0, pos - context_size)
                end = min(len(content), pos + context_size + len(word))
                context = content[start:end]

            if document not in inverted_index:
                inverted_index[document] = positions
    
        for filename, positions in inverted_index.items():
            file_path = os.path.join(document_folder, str(datetime.now().strftime('%Y%m%d')), filename + ".txt")
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                text = file.read()
                text_lower = text.lower().split()
                
                for value in positions:
                    start = max(0, value - context_size)
                    end = min(len(text_lower), value + context_size + len(word))
                    context = text_lower[start:end]
                    if filename not in contexts:
                        contexts[filename] = []
                    contexts[filename].append(context)

    return contexts if contexts else {}



