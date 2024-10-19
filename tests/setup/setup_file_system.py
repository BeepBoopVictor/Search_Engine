import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


def setup_books(count):
    directory = "tests\\test_repository"

    os.makedirs(directory, exist_ok=True)

    for i in range(count):
        with open(os.path.join(directory, f"book_{i + 1}.txt"), "w") as f:
            f.write(f"Este es el contenido del libro {i + 1}. Contiene texto sobre la libertad y los derechos. democracy\n")

