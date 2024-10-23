
def metadata_index_txt_store(metadata: dict, file: str):
    #with open(file, 'w') as f:
    #    f.truncate()  # Clear the content of the file

    with open(file, 'a') as f:
        for key, value in metadata.items():
            f.write(f"{{'{key}': {value}}}\n")
