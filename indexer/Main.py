import os, sys
from datetime import datetime
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from inverted_index.ProcessInvertedIndex import invertedIndex
from metadata.ProcessMetadataIndex import metadataIndex
from inverted_index.StoreMongoDBInvInd import inverted_index_from_mongodb
from inverted_index.StoreTXTInvInd import inverted_index_txt_store
from inverted_index.StoreNeo4JInvInd import inverted_index_store_neo4j
from loadBook.ReadTXTDocument import read_txt_as_dict
from metadata.StoreMongoDBMetadata import metadata_index_from_mongodb
from metadata.StoreNeo4JMetadata import metadata_store_neo4j
from metadata.StoreTXTMetadata import metadata_index_txt_store

class MyHandler(FileSystemEventHandler):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback

    def on_created(self, event):
        if not event.is_directory:
            self.callback(event.src_path)

def listener(actual_date, callback):
    # Waits until folder is created
    folder_path = os.path.join("datalake", actual_date)
    while not os.path.exists(folder_path):
        print(f"Folder {folder_path} doesn't exist yet. Waiting for it...")
        time.sleep(2) 

    event_handler = MyHandler(callback)
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=False)

    observer.start()
    print(f'Monitoring {folder_path} for new files...')

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def store_inverted_index(inverted, storage_type, additional_params=None):
    """ Stores the inverted index """

    # Store based on database
    if storage_type == "mongo":
        inverted_index_from_mongodb(inverted)
        print("Inverted index stored in MongoDB.")
    elif storage_type == "neo4j":
        inverted_index_store_neo4j(inverted)
        print("Inverted index stored in Neo4j.")
    elif storage_type == "txt":
        file_name = additional_params.get('file_name', 'inverted_index.txt')
        inverted_index_txt_store(inverted, file_name)   
        print(f"Inverted index stored in {file_name}.")
    else:
        print("Unsupported storage type")

def store_metadata(metadata, storage_type, additional_params=None):
    if storage_type == "mongo":
        metadata_index_from_mongodb(metadata)
        print("Metadata stored in MongoDB.")
    elif storage_type == "neo4j":
        metadata_store_neo4j(metadata)
        print("Metadata stored in Neo4j.")
    elif storage_type == "txt":
        file_name = additional_params.get('file_name', 'metadata.txt')
        metadata_index_txt_store(metadata, file_name)
        print(f"Metadata stored in {file_name}.")
    else:
        print("Unsupported storage type")

def process_new_file(actual_date):
    """ Process the new file when detected """
    file_path = os.path.join(actual_date)
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    documents = {}

    if file_path.endswith(".txt"):
        try:
            # Attempt to read the file with UTF-8 encoding
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
        except UnicodeDecodeError:
            try:
                # Fallback to ISO-8859-1 encoding
                with open(file_path, 'r', encoding='ISO-8859-1') as file:
                    content = file.read()
            except UnicodeDecodeError:
                try:
                    # Fallback to Windows-1252 encoding
                    with open(file_path, 'r', encoding='Windows-1252') as file:
                        content = file.read()
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
                    return  # Exit if all attempts fail

        documents[file_name] = content
        print(file_path+f"\\{file_name}")
        print(f"Processed document: {file_name}")

        # Proceed to create the inverted index and metadata
        inverted_index = invertedIndex(documents)
        metadata = metadataIndex(documents)

        # Store the inverted index and metadata
        store_inverted_index(inverted_index, "txt", {'file_name': 'datamart\\inverted_index.txt'})
        store_metadata(metadata, "txt", {'file_name': 'datamart\\metadata.txt'})
        store_inverted_index(inverted_index, "mongo")
        store_metadata(metadata, "mongo")
        store_inverted_index(inverted_index, "neo4j")
        store_metadata(metadata, "neo4j")


def actualizar_fecha():
    global fecha_actual
    fecha_actual = datetime.now().strftime('%Y%m%d')
    print(f"Fecha actualizada: {fecha_actual}")


def main():
    actualizar_fecha()
    listener(fecha_actual, process_new_file)

if __name__ == "__main__":
    main()
