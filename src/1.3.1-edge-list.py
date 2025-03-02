class Graph:
    def __init__(self):
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    def remove_edge(self, u, v):
        for edge in self.edges:
            if edge[1] == u and edge[2] == v:
                self.edges.remove(edge)
                break
            elif edge[1] == v and edge[2] == u:
                self.edges.remove(edge)
                break

    def display_edges(self):
        print("Edges:")

        for edge in self.edges:
            print(f"Edge {edge[1]} --{edge[0]}-> {edge[2]}")


graph = Graph()

graph.add_edge('A', 'B', 3)
graph.add_edge('A', 'D', 2)

graph.add_edge('A', 'C', 9)
graph.remove_edge('A', 'C')

graph.add_edge('B', 'C', 3)
graph.add_edge('B', 'D', 4)
graph.add_edge('D', 'C', 2)

graph.display_edges()
