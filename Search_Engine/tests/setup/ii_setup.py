import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from indexer.inverted_index.ProcessInvertedIndex import invertedIndex
from indexer.inverted_index.StoreMongoDBInvInd import inverted_index_from_mongodb
from indexer.inverted_index.StoreNeo4JInvInd import inverted_index_store_neo4j
from indexer.inverted_index.StoreTXTInvInd import inverted_index_txt_store


def read_txt_as_dict(file_path: str) -> dict:
    # Extracts the name of the file
    filename = file_path.split("\\")[-1].split(".")[0]

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        if isinstance(content, str):
            print("1")
            return {filename: content}
        else:
            print(f"Error: The content of {filename} is not a string, its {type(content)}.")
            return {filename: "ERROR_READING_FILE"}
    except UnicodeDecodeError:
        print(f"Error reading {file_path}. Trying with codification 'latin1'.")

        try:
            with open(file_path, 'r', encoding='latin1') as file:
                content = file.read()

            if isinstance(content, str):
                return {filename: content}
            else:
                print(f"Error: The content of {filename} is not a string, its {type(content)}.")
                return {filename: "ERROR_READING_FILE"} 

        except Exception as e:
            print(f"Error reading the file {file_path} with 'latin1': {e}")
            return {filename: "ERROR_READING_FILE"}

    except Exception as e:
        print(f"Error reading the file {file_path}: {e}")
        return {filename: "ERROR_READING_FILE"}

directory = "tests\\test_repository"
for archivo in os.listdir(directory):
    if archivo.endswith(".txt"):
        file_path = os.path.join(directory, archivo)
        datos_archivo = read_txt_as_dict(file_path)

        index = invertedIndex(datos_archivo)
        inverted_index_from_mongodb(index)
        #inverted_index_txt_store(index, "datamart\\inverted_index.txt")
        #inverted_index_store_neo4j(index)
