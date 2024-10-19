import os, ast, re, sys
from datetime import datetime
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Auxiliar function
def find_in_txt(word, file_path) -> dict:
    initial_pattern = rf"{{'{word}':"   # Pattern for the begining
    final_pattern   = r"\}\}$"          # Pattern for ending

    resultados = []
    bloque = ""
    capturando = False

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            if re.search(initial_pattern, line):
                capturando = True  
                bloque = line.strip()  

            elif capturando:
                bloque += " " + line.strip()

            if capturando and re.search(final_pattern, line):
                capturando = False  
                try:
                    diccionario = ast.literal_eval(bloque)
                    resultados.append(diccionario)
                except (SyntaxError, ValueError) as e:
                    print(f"Error al convertir a diccionario: {e}")
                bloque = ""
    return resultados[0] if resultados else None

def search_word_in_all_documents(word: str, directory: str):
    """
    Search the word in all the files from a directory.
    """
    word = word.lower()
    found_documents = []

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r') as file:
                    content = file.read().lower()
                    positions = [i for i, _ in enumerate(content.split()) if _ == word]

                if positions:
                    count = len(positions)
                    found_documents.append({"filename": filename, "positions": positions, "count": count})
                    print(f" - File: '{filename}', positions: {positions}, count: {count}")
            except Exception as e:
                print(f"Error reading the file '{filename}': {e}")

    if found_documents:
        return found_documents
    else:
        print(f"Word '{word}' not found.")
        return []


def search_multiple_words(words: list, file_path: str, match_all=True):
    """
    Search for multiple words in the indexed documents.
    """
    words = [word.lower() for word in words]
    results = {}

    inverted_index = {}

    for word in words:
        word_indexed = find_in_txt(word, file_path)
        key = list(word_indexed.keys())[0]
        value = word_indexed[key]
        inverted_index[key] = value

    for word in words:
        if word in inverted_index:
            for filename, positions in inverted_index[word].items():
                if filename not in results:
                    results[filename] = set()
                results[filename].update(positions)

    if match_all:
        matching_files = {filename: positions for filename, positions in results.items() if
                          all(word in inverted_index and filename in inverted_index[word] for word in words)}
        return matching_files
    else:
        return results

def search_documents(word: str, file_path: str):
    """
    Search for documents that contain a word without returning positions.
    """
    inverted_index = {}
    word = word.lower()

    word_indexed = find_in_txt(word, file_path)
    key = list(word_indexed.keys())[0]
    value = word_indexed[key]
    inverted_index[key] = value

    if word in inverted_index:
        return inverted_index
    else:
        return []

def search_word_with_context(word: str, file_path: str, document_folder: str, context_size: int = 30):
    """
    Search for a word and return the context around the occurrences in the documents.
    """
    word = word.lower()
    contexts = {}
    
    inverted_index = {}

    word_indexed = find_in_txt(word, file_path)
    key = list(word_indexed.keys())[0]
    value = word_indexed[key]
    inverted_index[key] = value

    if word in inverted_index:
        for filename, positions in inverted_index[word].items():
            file_path = os.path.join(document_folder, str(datetime.now().strftime('%Y%m%d')), filename + ".txt")
            print(file_path)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                text = file.read()
                text_lower = text.lower().split()

                for value in positions['positions']:
                    start = max(0, value - context_size)
                    end = min(len(text_lower), value + context_size + len(word))
                    context = text_lower[start:end]
                    if filename not in contexts:
                        contexts[filename] = []
                    contexts[filename].append(context)

    return contexts
