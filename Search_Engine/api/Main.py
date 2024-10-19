from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from endpoints.neo4j_search import router as neo4j_router
from endpoints.mongo_search import router as mongo_router
from endpoints.file_search import router as file_router
import uvicorn

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers from different modules
app.include_router(neo4j_router, prefix="/neo4j")
app.include_router(mongo_router, prefix="/mongodb")
app.include_router(file_router, prefix="/files")

if __name__ == "__main__":
    uvicorn.run("Main:app", host="127.0.0.1", port=8000, reload=True)
