class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = {}

        if v not in self.graph:
            self.graph[v] = {}

        self.graph[u][v] = weight

    def remove_edge(self, u, v):
        if u in self.graph:
            if v in self.graph[u]:
                del self.graph[u][v]

    def display_edges(self):
        print("Edges:")

        for node in self.graph:
            for (neighbor, cost) in self.graph[node].items():
                print(f"Edge {node} --{cost}-> {neighbor}")


graph = Graph()

graph.add_edge('A', 'B', 3)
graph.add_edge('A', 'D', 2)

graph.add_edge('A', 'C', 9)
graph.remove_edge('A', 'C')

graph.add_edge('B', 'A', 1)
graph.add_edge('B', 'C', 3)
graph.add_edge('B', 'D', 4)
graph.add_edge('C', 'B', 2)
graph.add_edge('C', 'D', 1)
graph.add_edge('D', 'C', 2)

graph.display_edges()
