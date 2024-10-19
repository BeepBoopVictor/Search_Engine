from collections import defaultdict
import re
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


def invertedIndex(books: dict) -> dict:
    index = defaultdict(lambda: defaultdict(lambda: {"positions": [], "count": 0}))
    
    for key, value in books.items():
        if isinstance(value, str):
            words = re.findall(r'\b\w+\b', value)

            for position, word in enumerate(words):
                word = word.lower()
                if word not in stop_words:
                    index[word][key]["positions"].append(position)
                    index[word][key]["count"] += 1
        else:
            print(f"Error: The content of {key} is not a string, its an {type(value)}.")

    index = {word: dict(files) for word, files in index.items()}
    
    return index

