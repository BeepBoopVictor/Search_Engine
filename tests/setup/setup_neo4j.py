from neo4j import GraphDatabase

def setup_books(count):
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "unodostres"))
    session = driver.session(database="books")

    session.run("MATCH (n) DETACH DELETE n")

    for i in range(count):
        session.run("CREATE (:Book {title: $title, content: $content})",
                    title=f"Book {i + 1}",
                    content=f"Este es el contenido del libro {i + 1}. Contiene texto sobre la libertad y los derechos.")

    session.close()

