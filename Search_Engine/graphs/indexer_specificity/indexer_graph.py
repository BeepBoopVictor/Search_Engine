import json
import matplotlib.pyplot as plt

# Ruta del archivo JSON
json_file_path = 'C:\\Users\\Usuario\\Desktop\\BENCHMARK\\0001_INDEXER.json.json'

# Cargar los datos desde el archivo JSON
with open(json_file_path, 'r') as file:
    data = json.load(file)  # Usa json.load para leer directamente del archivo


# Define groups
groups = {
    "process": ["process_MD", "process_II"],
    "store_ii": ["store_txt_ii", "store_mongo_ii", "store_neo4j_ii"],
    "store_md": ["store_txt_md", "store_mongo_md", "store_neo4j_md"],
}

# Create graphs for each group
for group_name, group_items in groups.items():
    plt.figure(figsize=(10, 6))
    for item in group_items:
        # Filter for statistics
        stats = next((benchmark for benchmark in data['benchmarks'] if benchmark['group'] == item), None)
        if stats:
            # Extract values
            means = stats['stats']['mean']
            stddev = stats['stats']['stddev']
            plt.bar(item, means, yerr=stddev, label=item)

    plt.title(f'Mean Execution Time for {group_name}')
    plt.ylabel('Time (seconds)')
    plt.xlabel('Benchmark Functions')
    plt.xticks(rotation=45)

    # Set y-axis to logarithmic scale for store_ii group
    if group_name == "store_ii":
        plt.yscale('log')

    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{group_name}_benchmark_graph.png")  # Save the graph as an image
plt.show()
