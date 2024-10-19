import os, sys, pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(sys.path)
from query_engine.metadata_queries.metadata_mongoDB_query import *
from query_engine.metadata_queries.metadata_neo4j_query import *
from query_engine.metadata_queries.metadata_query import *
import query_engine.word_queries.file_query_engine as txt_word
import query_engine.word_queries.mongo_DB_query_engine as mdb_word
import query_engine.word_queries.neo4j_query_engine as neo4j_word

from indexer.inverted_index.ProcessInvertedIndex import invertedIndex

def process_documents_from_folder(folder_path):
    """ Read every txt folder and create a dictionary """
    documents = {}
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            documents[file_name] = content
    return documents

book = process_documents_from_folder("..\\datalake\\20241019") # Load correct date

ii = invertedIndex(book)

summed_word_dict = {}

for word, files in ii.items():
    total_count = sum(file_data['count'] for file_data in files.values())
    summed_word_dict[word] = total_count

sorted_word_dict = dict(sorted(summed_word_dict.items(), key=lambda item: item[1], reverse=True))
top_10 = list(sorted_word_dict.items())[:5]

bottom_10 = list(sorted_word_dict.items())[-5:]



# -------------------------       WORD QUERIES       ------------------------------


@pytest.mark.benchmark(group="query_txt_freq")
@pytest.mark.parametrize("word", [w for w, _ in top_10])
def test_txt_query_II_freq(benchmark, word):
    benchmark(txt_word.search_word_in_all_documents, word, "..\\datalake")

@pytest.mark.benchmark(group="query_mongo_freq")
@pytest.mark.parametrize("word", [w for w, _ in top_10])
def test_mongo_query_II_freq(benchmark, word):
    benchmark(mdb_word.search_word_in_all_documents, word)

@pytest.mark.benchmark(group="query_neo4j_freq")
@pytest.mark.parametrize("word", [w for w, _ in top_10])
def test_neo_query_II_freq(benchmark, word):
    benchmark(neo4j_word.search_word_in_all_documents, word)




@pytest.mark.benchmark(group="query_txt_unfreq")
@pytest.mark.parametrize("word", [w for w, _ in bottom_10])
def test_txt_query_II_unfreq(benchmark, word):
    benchmark(txt_word.search_word_in_all_documents, word, "..\\datalake")

@pytest.mark.benchmark(group="query_mongo_unfreq")
@pytest.mark.parametrize("word", [w for w, _ in bottom_10])
def test_mongo_query_II_unfreq(benchmark, word):
    benchmark(mdb_word.search_word_in_all_documents, word)

@pytest.mark.benchmark(group="query_neo4j_unfreq")
@pytest.mark.parametrize("word", [w for w, _ in bottom_10])
def test_neo_query_II_unfreq(benchmark, word):
    benchmark(neo4j_word.search_word_in_all_documents, word)
