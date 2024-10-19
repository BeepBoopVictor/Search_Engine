from fastapi import APIRouter, HTTPException
import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from query_engine.word_queries.file_query_engine import (
    search_documents,
    search_word_with_context,
)

router = APIRouter()

@router.get("/search/")
async def search_word(word: str):
    """
    Search for a word in the indexed documents.
    """
    results = search_documents(word, "datamart\\inverted_index.txt")
    if results:
        return {f"results": results}
    else:
        raise HTTPException(status_code=404, detail=f"The word '{word}' was not found in the documents.")



@router.get("/search/context/")
async def search_word_with_context_endpoint(word: str, context_size: int = 30):
    """
    Search for a word with context in the indexed documents.
    """
    contexts = search_word_with_context(word, "datamart\\inverted_index.txt", "datalake", context_size)
    text_data = {key: [' '.join(paragraph) for paragraph in paragraphs] for key, paragraphs in contexts.items()}
    if contexts:
        return {"contexts": text_data}
    else:
        raise HTTPException(status_code=404, detail=f"The word '{word}' was not found in the documents.")

