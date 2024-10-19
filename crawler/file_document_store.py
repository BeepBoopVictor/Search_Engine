import sys
from datetime import datetime
from abc import ABC
import os
import errno
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class FileDocumentStore(ABC):
    DOCUMENT_REPOSITORY_PATH = "datalake"

    def save_document(self, document: str, composed_id: str):
        if document is None:
            raise ValueError("Document cannot be null")

        document_date = self.extract_date_from_id(composed_id)
        self.create_folder_if_not_exists(document_date)
        self.create_file(document, document_date)

    def create_file(self, document, document_date: datetime):
        # Obteins the name of the current folder based on the date
        folder_path = self.generate_folder_path(document_date)

        # Obteins number of books in the folder
        book_number = self.get_next_book_number(folder_path)

        # Generates the name as book_<number>.txt
        file_name = f"book_{book_number}.txt"
        file_path = os.path.join(folder_path, file_name)

        try:
            with open(file_path, 'w', encoding='utf-8') as writer:
                writer.write(str(document))  # Store the document
            print(f"Document saved to: {file_path}")
        except IOError as e:
            print(f"Error writing file: {e}")
            raise  # Re-throws the exception to be handled by the caller if necessary

    def create_folder_if_not_exists(self, document_date: datetime):
        folder_path = self.generate_folder_path(document_date)
        if not os.path.exists(folder_path):
            try:
                os.makedirs(folder_path)
                print(f"Directory created: {folder_path}")
            except OSError as e:
                if e.errno != errno.EEXIST:
                    print(f"Failed to create directory: {folder_path}")
                    raise

    def generate_folder_path(self, document_date: datetime) -> str:
        # Creates the folder based on the actual date
        folder_date = document_date.strftime("%Y%m%d")
        return os.path.join(self.DOCUMENT_REPOSITORY_PATH, folder_date)

    def extract_date_from_id(self, composed_id: str) -> datetime:
        # Extracts the date from composed_id
        date_str = composed_id.split("/")[0]  # Obtener la parte de la fecha
        return datetime.strptime(date_str, "%Y-%m-%d %H-%M-%S")

    def get_next_book_number(self, folder_path: str) -> int:
        # Obteins the next book
        existing_books = [f for f in os.listdir(folder_path) if f.startswith("book_") and f.endswith(".txt")]

        if not existing_books:
            return 1  # If there are no books it returns 1

        # Extracts the current number of books and return the last one
        book_numbers = [int(f.split('_')[1].split('.')[0]) for f in existing_books]
        return max(book_numbers) + 1
