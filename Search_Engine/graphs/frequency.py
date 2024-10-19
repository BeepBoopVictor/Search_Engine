import json, sys, os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the JSON file
with open('frequency\\0002_FREQUENCY.json') as f:
    data = json.load(f)

# Extract relevant data
benchmarks = data['benchmarks']

# Prepare a list to store data
records = []

# Gather the mean times for each benchmark
for benchmark in benchmarks:
    group = benchmark['group']
    word = benchmark['param']
    mean_time = benchmark['stats']['mean']
    records.append({
        'Group': group.split('_')[1],  # Get txt, mongo, or neo4j
        'Word': word,
        'Mean Time (s)': mean_time
    })

# Convert to a DataFrame for better manipulation
df = pd.DataFrame(records)

# Create the plot
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Word', y='Mean Time (s)', hue='Group')

# Customize the plot
plt.title('Mean Time Comparison by Group and Word')
plt.xlabel('Queried Word')
plt.ylabel('Mean Time (seconds)')
plt.legend(title='Query Group')

# Display the plot
plt.tight_layout()
plt.show()
