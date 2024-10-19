from neo4j import GraphDatabase

# Connect to neo4j
uri         = "neo4j://localhost:7687"
user        = "neo4j"
password    = "unodostres"
driver      = GraphDatabase.driver(uri, auth=(user, password))

# Function to store a whole dictionary
def metadata_store_neo4j(metadata: dict):

    with driver.session(database="metadata") as session:
        for key, value in metadata.items():
            session.run(
                """
                MERGE (f:File {name: $key})
                ON CREATE SET f.author = $author, f.date = $date, f.language = $language
                RETURN f
                """,
                key=key, author=value['author'], date=value['date'], language=value['language']   
                )


