import re ,ast, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


def search_by_author(file_path: str, author: str) -> dict:
    results = {}
    print(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            print(line)
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


def search_by_date(file_path: str, date: str) -> dict:
    results = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
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


def search_by_language(file_path: str, language: str) -> dict:
    results = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
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
