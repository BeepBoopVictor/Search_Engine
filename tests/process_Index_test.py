import os, pytest, sys
    
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from indexer.inverted_index.ProcessInvertedIndex import invertedIndex
from indexer.inverted_index.StoreMongoDBInvInd import inverted_index_from_mongodb
from indexer.inverted_index.StoreNeo4JInvInd import inverted_index_store_neo4j
from indexer.inverted_index.StoreTXTInvInd import inverted_index_txt_store
from indexer.metadata.ProcessMetadataIndex import metadataIndex
from indexer.metadata.StoreMongoDBMetadata import metadata_index_from_mongodb
from indexer.metadata.StoreNeo4JMetadata import metadata_store_neo4j
from indexer.metadata.StoreTXTMetadata import metadata_index_txt_store

def process_documents_from_folder(folder_path):
    """ Reads the txt folder  """
    documents = {}
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            documents[file_name] = content
    print(type(documents))
    return documents

@pytest.fixture
def books():
    return process_documents_from_folder("..\\datalake\\20241019")

@pytest.fixture
def ii(books):
    return invertedIndex(books)

@pytest.fixture
def md(books):
    return metadataIndex(books)

# -----------------------------    PROCESS INVERTED INDEX     --------------------------------------------

@pytest.mark.benchmark(group="process_II")
def test_process_inverted_index(benchmark, books):
    benchmark(invertedIndex, books)

# -----------------------------      PROCESS METADATA        --------------------------------------------

@pytest.mark.benchmark(group="process_MD")
def test_process_metadata(benchmark, books):
    benchmark(metadataIndex, books)

# -----------------------------    STORE INVERTED INDEX       --------------------------------------------

@pytest.mark.benchmark(group="store_txt_ii")
def test_txt_store_II(benchmark, ii):
    benchmark(inverted_index_txt_store, ii, "..\\datamart\\inverted_index.txt")

@pytest.mark.benchmark(group="store_mongo_ii")
def test_mongodb_store_II(benchmark, ii):
    benchmark(inverted_index_from_mongodb, ii)

@pytest.mark.benchmark(group="store_neo4j_ii")
def test_neo4j_store_II(benchmark, ii):
    benchmark(inverted_index_store_neo4j, ii)


# -----------------------------        STORE METADATA         --------------------------------------------

@pytest.mark.benchmark(group="store_txt_md")
def test_txt_store_MD(benchmark, md):
    benchmark(metadata_index_txt_store, md, "..\\datamart\\metadata.txt")

@pytest.mark.benchmark(group="store_mongo_md")
def test_mongodb_store_MD(benchmark, md):
    benchmark(metadata_index_from_mongodb, md)

@pytest.mark.benchmark(group="store_neo4j_md")
def test_neo4j_store_MD(benchmark, md):
    benchmark(metadata_store_neo4j, md)
