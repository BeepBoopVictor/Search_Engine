
def read_txt_as_dict(file_path: str) -> dict:
    # Extracts the name of the file without the extension
    filename = file_path.split("/")[-1].split(".")[0]

    try:
        # Tries to open with codification 'utf-8'
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        if isinstance(content, str):
            print("1")
            return {filename: content}
        else:
            print(f"Error: The content of {filename} is not a string, its {type(content)}.")
            return {filename: "ERROR_READING_FILE"}

    except UnicodeDecodeError:
        print(f"Error reading the file {file_path}. Trying with codification 'latin1'.")

        try:
            with open(file_path, 'r', encoding='latin1') as file:
                content = file.read()

            if isinstance(content, str):
                return {filename: content}
            else:
                print(f"Error: The content of {filename} is not a string, its {type(content)}.")
                return {filename: "ERROR_READING_FILE"}  # Si no es cadena, marcar como error

        except Exception as e:
            print(f"Error reading the file {file_path} con 'latin1': {e}")
            return {filename: "ERROR_READING_FILE"}

    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return {filename: "ERROR_READING_FILE"}
