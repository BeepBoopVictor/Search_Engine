import re


def metadataIndex(book: dict) -> dict:
    metadata_index = {}

    author_regex        = re.compile(r'^Author:\s*(.*)', re.IGNORECASE | re.MULTILINE)
    release_date_regex  = re.compile(r'^Release date:\s*(.*)', re.IGNORECASE | re.MULTILINE)
    language_regex      = re.compile(r'^Language:\s*(.*)', re.IGNORECASE | re.MULTILINE)

    for key, value in book.items():
        text = value

        author        = author_regex.search(text)
        release_date  = release_date_regex.search(text)
        language      = language_regex.search(text)

        metadata_index[key] = {
            "author"   : author.group(1) if author else "Not found",
            "date"     : release_date.group(1) if release_date else "Not found",
            "language" : language.group(1) if language else "Not found"
        }

    return metadata_index
