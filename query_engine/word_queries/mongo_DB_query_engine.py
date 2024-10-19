import re, sys, os
from pymongo import MongoClient
from datetime import datetime
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

client = MongoClient("mongodb://localhost:27017/")
db = client["book_search_engine"]  # Database
index_collection = db["invertedindex"]  # Collection to store the inverted index

def search_word_in_all_documents(word: str):
    word = word.lower() 
    result = index_collection.find_one({"word": word})
    print(result)
    if result:
        documents = result["files"]
        if documents:
            found_documents = []
            print(f"Word '{word}' found in the next documents:")
            for book_id, positions in documents.items():
                found_documents.append({"book_id": book_id, "positions": positions})
                print(f" - Document with ID: {book_id}, positions: {positions}")
            return found_documents 
        else:
            print(f"Word '{word}' found, but not in any document.")
            return [] 
    else:
        print(f"Word '{word}' not found in any documents.")
        return []


def search_multiple_words(words: list, match_all=True):
    """
    Search for multiple words in MongoDB documents.
    """
    words = [word.lower() for word in words]
    query_results = list(index_collection.find({"word": {"$in": words}}))

    if match_all:
        # Intersection of results to match all words (AND)
        matching_docs = {}
        for result in query_results:
            if "documents" in result:
                for doc_id, positions in result["documents"].items():
                    if doc_id not in matching_docs:
                        matching_docs[doc_id] = set(positions)
                    else:
                        matching_docs[doc_id].intersection_update(positions)
        return matching_docs
    else:
        matching_docs = {}
        for result in query_results:
            if "documents" in result:
                for doc_id, positions in result["documents"].items():
                    if doc_id not in matching_docs:
                        matching_docs[doc_id] = set(positions)
                    else:
                        matching_docs[doc_id].update(positions)
        return matching_docs


def search_documents(word: str):
    """
    Search for documents that contain a word without returning positions.
    """
    word = word.lower()
    result = index_collection.find_one({"word": word})

    if result and "documents" in result:
        return list(result["documents"].keys())
    else:
        return []


def search_word_with_context(word: str, folder_path: str, context_size: int = 30):
    """
    Search for a word and return the context around its occurrences in the documents.
    """
    word = word.lower()
    result = index_collection.find_one({"word": word})
    contexts = {}
    if word in result['word']:
        for filename, positions in result['files'].items():
            file_path = os.path.join(folder_path, str(datetime.now().strftime('%Y%m%d')), filename + ".txt")
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                text = file.read()
                text_lower = text.lower().split()
                print(positions)
                for value in positions[0][0]:

                    start = max(0, value - context_size)
                    end = min(len(text_lower), value + context_size + len(word))
                    context = text_lower[start:end]
                    if filename not in contexts:
                        contexts[filename] = []
                    contexts[filename].append(context)

    return contexts

