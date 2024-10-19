import re ,ast

def search_by_author(file_path: str, authors: list) -> dict:
    results = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            for author in authors:
                # Create a pattern for the author
                pattern = rf"'author': '{re.escape(author)}'"
                if re.search(pattern, line):
                    # Convert the line to a dictionary
                    try:
                        entry = ast.literal_eval(line.strip())
                        results.update(entry)  # Add the dictionary
                    except (SyntaxError, ValueError) as e:
                        print(f"Error processing: {line.strip()} - {e}")
    
    return results

def search_by_date(file_path: str, dates: list) -> dict:
    results = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            for date in dates:
                # Create a pattern for the date
                pattern = rf"'date': '{re.escape(date)}'"
                if re.search(pattern, line):
                    # Convert the line to a dictionary
                    try:
                        entry = ast.literal_eval(line.strip())
                        results.update(entry)  # Add the dictionary
                    except (SyntaxError, ValueError) as e:
                        print(f"Error processing: {line.strip()} - {e}")
    
    return results


def search_by_language(file_path: str, languages: list) -> dict:
    results = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            for language in languages:
                # Create a pattern for the language
                pattern = rf"'language': '{re.escape(language)}'"
                if re.search(pattern, line):
                    # Convert the line to dictionary
                    try:
                        entry = ast.literal_eval(line.strip())
                        results.update(entry)  # Add the dictionary
                    except (SyntaxError, ValueError) as e:
                        print(f"Error processing: {line.strip()} - {e}")
    
    return results


