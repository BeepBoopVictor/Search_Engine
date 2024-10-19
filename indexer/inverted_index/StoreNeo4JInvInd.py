from neo4j import GraphDatabase

# Connect to neo4j
uri         = "neo4j://localhost:7687"
user        = "neo4j"
password    = "unodostres"
driver      = GraphDatabase.driver(uri, auth=(user, password))


def inverted_index_store_neo4j(inverted: dict):
    with driver.session(database="invertedindex") as session:
        for word, docs in inverted.items():
            for title, positions in docs.items():
                try:
                    session.run(
                        """
                        MERGE (d:Document {title: $title})
                        MERGE (w:Word {word: $word})
                        MERGE (w)-[r:APPEARS_IN]->(d)
                        ON CREATE SET r.positions = $positions, w.count = $count
                        ON MATCH SET r.positions = COALESCE(r.positions, []) + $positions, w.count = w.count
                        """,
                        title=title, word=word, positions=positions['positions'], count=positions['count']
                    )
                except Exception as e:
                    print(f"Error inserting word '{word}' in document '{title}': {e}")

