import requests
from bs4 import BeautifulSoup

class GutenbergDocumentDownloader:
    URL_PROJECT_GUTENBERG = "https://www.gutenberg.org/cache/epub/{id}/pg{id}.txt"


    def download_document(self, book_id: int):
        book_url = self.URL_PROJECT_GUTENBERG.replace("{id}", str(book_id))
        print(book_url)
        try:
            response = requests.get(book_url)
            response.raise_for_status()  # Raises an exception if the request fails
            document_text = response.text
            return BeautifulSoup(document_text, 'html.parser')  # Returns the content as a BeautifulSoup object
        except requests.RequestException as e:
            print(f"Error downloading the document: {e}")
            raise
