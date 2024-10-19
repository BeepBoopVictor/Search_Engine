import time
import threading
from datetime import datetime
from requests.exceptions import RequestException

class DocumentController:

    def __init__(self, downloader, document_store, n_documents: int):
        self.downloader = downloader
        self.document_store = document_store
        self.book_id_counter = 1  # Start the counter at 1
        self.timer = threading.Timer  # We will use threading to schedule periodic tasks
        self.n = n_documents


    def start_crawler(self):
        self.schedule_downloads()


    def schedule_downloads(self):
        # Schedule the download every minute
        def run_task():
            while True:
                for _ in range(self.n): 
                    next_book_id = self.get_next_book_id()
                    self.process_document(next_book_id)
                time.sleep(60)  # 1-minute interval between downloads

        # Start a thread that runs the task repeatedly
        threading.Thread(target=run_task, daemon=True).start()


    def process_document(self, book_id):
        try:
            # Download the document from the URL using the updated method
            document = self.downloader.download_document(book_id)
            current_date = datetime.now()  # Use the current date to store the document

            # Format the date as part of the composed index
            formatted_date = current_date.strftime('%Y-%m-%d %H-%M-%S')
            composed_id = f"{formatted_date}/{book_id}"  # Create a composed index with date and book_id

            # Store the document in the repository with the composed index
            self.document_store.save_document(document, composed_id)

            print(f"Successfully saved document with ID: {composed_id}")
        except RequestException as e:
            self.handle_error(e)


    def handle_error(self, e):
        print(f"Error occurred: {e}")
        # Handle the exception and optionally print additional details for debugging


    def get_next_book_id(self):
        # Generate a new book ID sequentially
        self.book_id_counter += 1
        return self.book_id_counter
