
def metadata_index_txt_store(metadata: dict, file: str):
    with open(file, 'a') as f:
        for key, value in metadata.items():
            f.write(f"{{'{key}': {value}}}\n")
