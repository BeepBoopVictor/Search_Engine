# Search Engine Project

## Cover Page:

- *Subject:* Big Data (BD)
- *Academic Year:* 2024-2025
- *Degree:* Data Science and Engineering (GCID)
- *School:* School of Computer Engineering (EII)
- *University:* University of Las Palmas de Gran Canaria (ULPGC)

## Project Overview:

This project implements a comprehensive search engine designed to process and query large volumes of textual data, utilizing key principles from Big Data management. The system allows for efficient document crawling, indexing, and querying, making it a robust solution for handling large-scale document retrieval and analysis.

## Main Functionality:

- *Document Crawling*: The crawler component downloads and stores documents from Project Gutenberg, into a datalake for further processing.
- *Data Indexing*: The indexer component processes the documents and creates an inverted index, as well as metadata structure, which enables fast search and retrieval of terms.
- *Query Engine*: The query_engine allows users to perform queries on the indexed documents, providing search capabilities based on words and metadata.
- *Data Visualization*: The graphs component offers scripts to generate visual representations of the data, including word frequency and indexing metrics.

## Project Structure:

- *Crawler*: Downloads and stores documents, ensuring they are available for indexing.
- *Datalake*: Serves as the repository for raw and unprocessed data.
- *Datamart*: Contains processed data, including the inverted index and metadata for fast querying.
- *Indexer*: Manages the indexing of documents into efficient search structures.
- *Query Engine*: Provides the main functionality for querying indexed documents.
- *API*: Handles API interactions and endpoints for document and query management.
- *UI*: A user-friendly interface that allows users to interact with the search engine.
- *Test*: By using benchmark tools, it provides useful data about the time execution, scalability, etc.
- *Graphs*: Generates visualizations to analyze the indexing and query performance.

## Development Environment:

- *Development Environment*: PyCharm.
- *Version Control*: Git & GitHub for source code management and collaboration.

## How to Run the Program:

1. *Install Requirements*: 
   Ensure that all dependencies listed in the requirements.txt are installed by running:
   bash
   pip install -r requirements.txt
   
2. *Running the Crawler*: 
   The document crawler can be executed by navigating to the crawler directory and running:
   bash
   python 
   
3. *Running the Indexer*: 
   To process the crawled documents and generate an inverted index and metadata structure, navigate to the indexer folder:
   bash
   python 
   
4. *Executing Queries*: 
   You can query the indexed documents by running the query engine in the query_engine folder:
   bash
   python 

5. *Executing API*: 
   You can verify the results of the query module by using the API Rest. There are three different one, each one for its data strcuture (File System, Mongo DB or Neo4j). In the local host, use the port 8000 to try the inputs.
   bash
   python
6. *Tests*: 
   You can test, which use benchmark, the different data structure in your computer by running the tests files.
   bash
   python
7. *Generating Graphs (Optional)*: 
   Visualizations can be created by running the scripts in the graphs folder. For example, to generate word frequency graphs:
   bash
   python 
   
## SOLID Principles:
   This project adheres to the SOLID principles to ensure maintainable and scalable code.
-  *Single Responsibility Principle*: Each module or class handles a single responsibility or functionality.
-  *Open/Closed Principle*: The system is open for extension but closed for modification, making it flexible for future enhancements.
-  *Interface Segregation Principle*: Interfaces are designed to be specific, avoiding "fat" interfaces and ensuring that classes only depend on methods they use. However, due to Python's limitations this principle is more challenging to implement strictly.

## Testing:
   Unit and performance tests are located in the 'tests' directory.
-  Unit tests ensure that individual components, such as the crawler, indexer, and query engine, work correctly.
  - Benchmarking tests evaluate the system's performance under different conditions, ensuring it can handle large datasets efficiently.

## Other Highlights:
-  *Scalability*: The architecture is built to scale, capable of processing and indexing large volumes of data efficiently.
- *Modularity*: The project is modular, with components designed to be self-contained, making them reusable and easy to debug.
- *Visualization*: Graph scripts provide insights into the data, such as word frequency and indexing patterns, helping users analyze trends and performance metrics in the dataset. 

### Participants:
-      María Alonso León
-      Víctor Gil Bernal
-      Jacob Jażdżyk
-      Kimberly Casimiro Torres
