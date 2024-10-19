import json
import matplotlib.pyplot as plt

# Load data from the JSON file
with open('/mnt/data/0001_multiple_books_benchmark.json', 'r') as f:
    data = json.load(f)

# Initialize lists to store execution times by technology
file_system = []
mongo = []
neo4j = []
counts = []

# Process the data
for benchmark in data['benchmarks']:
    count = int(benchmark['param'])  # Number of entries (count)
    
    if "file_system" in benchmark['name']:
        file_system.append(benchmark['stats']['mean'])
    elif "mongo_db" in benchmark['name']:
        mongo.append(benchmark['stats']['mean'])
    elif "neo4j" in benchmark['name']:
        neo4j.append(benchmark['stats']['mean'])
    
    if count not in counts:
        counts.append(count)

# Plot the results
plt.figure(figsize=(10, 6))

# Line charts with elegant colors
plt.plot(counts, file_system, label='File System', marker='o', color='darkcyan', linewidth=2)
plt.plot(counts, mongo, label='MongoDB', marker='s', color='royalblue', linewidth=2)
plt.plot(counts, neo4j, label='Neo4j', marker='^', color='crimson', linewidth=2)

# Titles and labels
plt.title('Comparison of Search Times: File System vs MongoDB vs Neo4j', fontsize=14, fontweight='bold')
plt.xlabel('Number of documents queried', fontsize=12)
plt.ylabel('Average execution time (seconds)', fontsize=12)
plt.legend()

# Show the plot
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
