import os, ast

def inverted_index_txt_store(inverted: dict, file: str):
    # Check if the inverted index is empty
    if not inverted:
        print("The inverted index is empty. Nothing will be written.")
        return

    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(file), exist_ok=True)

    # Try to read the existing data from the file (if needed)
    try:
        # Read the existing inverted index from the file
        if os.path.exists(file):
            with open(file, 'r') as f:
                existing_data = f.readlines()
                
            # Convert the existing lines to a dictionary
            existing_inverted_index = {}
            for line in existing_data:
                # Use ast.literal_eval to safely parse the line into a dictionary
                entry = ast.literal_eval(line.strip())
                existing_inverted_index.update(entry)
        else:
            existing_inverted_index = {}

    except Exception as e:
        print(f"Error reading from the file: {e}")
        return

    # Update the existing inverted index with new entries
    for word, new_book_data in inverted.items():
        if word in existing_inverted_index:
            # If the word exists, update the positions for each book
            for book_path, positions in new_book_data.items():
                if book_path in existing_inverted_index[word]:
                    # If the book already exists for this word, update positions
                    existing_inverted_index[word][book_path] = list(set(existing_inverted_index[word][book_path] + positions))
                else:
                    # Add a new book entry for this word
                    existing_inverted_index[word][book_path] = positions
        else:
            # If the word doesn't exist, add the entire word entry
            existing_inverted_index[word] = new_book_data

    # Write the updated inverted index back to the file
    try:
        with open(file, 'w') as f:
            for key, value in existing_inverted_index.items():
                # Write in the specified format
                f.write(f"{{'{key}': {value}}}\n")
        print(f"File written correctly: {file}")
    except Exception as e:
        print(f"Error writing the file: {e}")
