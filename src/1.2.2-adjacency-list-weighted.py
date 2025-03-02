graph = {
    'A': { 'B': 3, 'D': 2 },
    'B': { 'A': 1, 'C': 3, 'D': 4 },
    'C': { 'B': 2, 'D': 1 },
    'D': { 'C': 2 }
}

print("Edges:")

for node in graph:
    for (neighbor, cost) in graph[node].items():
        print(f"Edge {node} --{cost}-> {neighbor}")
