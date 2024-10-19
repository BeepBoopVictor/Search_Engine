from fastapi import APIRouter, HTTPException
from query_engine.metadata_queries.metadata_mongoDB_query import *

router_m = APIRouter()


@router_m.get("/search/author/")
async def search_author(author: str):
    """
    Author search.
    """
    results = search_by_author(author)
    if results:
        return {"results": results}
    else:
        raise HTTPException(status_code=404, detail="Documents not found.")

@router_m.get("/search/date/")
async def search_date(date: str):
    """
    Date search.
    """
    results = search_by_date(date)
    if results:
        return {"results": results}
    else:
        raise HTTPException(status_code=404, detail="Documents not found.")

@router_m.get("/search/language/")
async def search_language(language: str):
    """
    Language search.
    """
    results = search_by_language(language)
    if results:
        return {"results": results}
    else:
        raise HTTPException(status_code=404, detail="Documents not found.")
