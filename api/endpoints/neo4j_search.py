from fastapi import APIRouter, HTTPException
import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from query_engine.word_queries.neo4j_query_engine import (
    search_word_in_all_documents,
    search_word_with_context
)

router = APIRouter()

@router.get("/search/")
async def search_word(word: str):
    """
    Search for a word in the indexed documents in Neo4j.
    """
    matches = search_word_in_all_documents(word)
    if matches:
        return {f"results for \'{word}\'": matches}
    else:
        raise HTTPException(status_code=404, detail=f"The word '{word}' was not found in any document.")


@router.get("/search/context/")
async def search_with_context(word: str, context_size: int = 30):
    '''
    Search for a word and return context.
    '''
    contexts = search_word_with_context(word, "datalake", context_size)
    text_data = {key: [' '.join(paragraph) for paragraph in paragraphs] for key, paragraphs in contexts.items()}
    if contexts:
        return {"results": text_data}
    else:
        raise HTTPException(status_code=404, detail=f"No context found for the word '{word}'.")
