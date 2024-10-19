import os, sys, pytest, random

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

#from tests.setup.setup_file_system import setup_books as setup_books_file
#from tests.setup.setup_mongo_db import setup_books as setup_books_mongo
#from tests.setup.setup_neo4j import setup_books as setup_books_neo4j

from query_engine.word_queries.file_query_engine import search_word_in_all_documents as search_fs
from query_engine.word_queries.mongo_DB_query_engine import search_word_in_all_documents as search_mongo
from query_engine.word_queries.neo4j_query_engine import search_word_in_all_documents as search_neo4j

book_counts = [10, 50, 100, 500, 1000]
search_words = ["freedom", "rights", "constitution", "democracy", "law"]

@pytest.mark.parametrize("count", book_counts)
@pytest.mark.benchmark(group="file_search")
def test_file_system_search(benchmark, count):
    #setup_books_file(count)
    word = random.choice(search_words)

    result = benchmark(search_fs, word, "..\\..\\datamart")

    print(f"Resultados para {count} libros: {result}")

    assert result is not None

@pytest.mark.parametrize("count", book_counts)
@pytest.mark.benchmark(group="mongo_search")
def test_mongo_db_search(benchmark, count):
    #setup_books_mongo(count)
    word = random.choice(search_words)

    result = benchmark(search_mongo, word)

    assert result is not None

@pytest.mark.parametrize("count", book_counts)
@pytest.mark.benchmark(group="neo4j_search")
def test_neo4j_search(benchmark, count):
    #setup_books_neo4j(count)
    word = random.choice(search_words)
    result = benchmark(search_neo4j, word)
    assert result is not None
