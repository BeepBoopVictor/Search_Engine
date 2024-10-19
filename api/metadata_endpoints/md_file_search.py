from fastapi import APIRouter, HTTPException
import sys, os
from api.metadata_endpoints.load_metadata import load_from_txt
from query_engine.metadata_queries.metadata_query import *
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
router_m = APIRouter()


metadata = load_from_txt("datamart\\metadata.txt")


@router_m.get("/search/author/")
async def search_author(author: str):
    """
    Author search.
    """
    print(f"Received authors: {author}")
    results = search_by_author(metadata, author)
    if results:
        return {"title": results}
    else:
        raise HTTPException(status_code=404, detail="No documents matched the search terms.")



@router_m.get("/search/date/")
async def search_author(date: str):
    """
    Date search.
    """
    results = search_by_date(metadata, date)
    if results:
        return {"date": results}
    else:
        raise HTTPException(status_code=404, detail="No documents matched the search terms.")


@router_m.get("/search/language/")
async def search_title(language: str):
    """
    Language search.
    """
    results = search_by_language(metadata, language)
    if results:
        return {"languaje": results}
    else:
        raise HTTPException(status_code=404, detail=f"No documents matched the search terms.")
