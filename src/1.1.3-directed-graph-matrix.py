class Graph:
    def __init__(self, size):
        self.matrix = [[0] * size for _ in range(size)]
        self.size = size

    def add_edge(self, u, v):
        self.matrix[u][v] = 1

    def display_matrix(self):
        print("Adjacency Matrix:")

        for row in self.matrix:
            print(row)

    def display_edges(self):
        print("Edges:")

        for u in range(self.size):
            for v in range(self.size):
                if self.matrix[u][v] == 1:
                    print(f"Edge {u} -> {v}")


graph = Graph(4)

graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 0)

graph.display_matrix()
graph.display_edges()
