import threading

# Let's assume the following classes are already defined as before
from gutenberg_document_downloader import GutenbergDocumentDownloader
from file_document_store import FileDocumentStore
from document_controller import DocumentController

# Create an instance of the downloader for Project Gutenberg
downloader = GutenbergDocumentDownloader()

n_documents = 5

document_store = FileDocumentStore()
# Create an instance of the controller to coordinate the download and storage of documents
controller = DocumentController(downloader, document_store, n_documents)

# Start the download and storage process
controller.start_crawler()

# Use threading to keep the program running
latch = threading.Event()
print("Document Crawler started. Press Ctrl+C to stop.")

try:
    latch.wait()  # Wait indefinitely
except KeyboardInterrupt:
    print("Process interrupted.")
