class GraphMatrix:
    def __init__(self, size):
        self.matrix = [[None] * size for _ in range(size)]
        self.size = size

    def add_edge(self, u, v, weight):
        position_u = self.__get_coordinate(u)
        position_v = self.__get_coordinate(v)

        if position_u == position_v:
            raise ValueError("The edge must not be a loop")

        self.matrix[position_u][position_v] = weight

    def remove_edge(self, u, v):
        position_u = self.__get_coordinate(u)
        position_v = self.__get_coordinate(v)

        if position_u == position_v:
            raise ValueError("The edge must not be a loop")

        self.matrix[position_u][position_v] = None

    def display_matrix(self):
        print("Adjacency Matrix:")

        print(" ", end=" ")
        for i in range(self.size):
            print(chr(i + ord('A')), end=" ")

        print()
        for i in range(self.size):
            print(chr(i + ord('A')), end=" ")
            for j in range(self.size):
                print(self.matrix[i][j] if self.matrix[i][j] is not None else '-', end=" ")
            print()

    def display_edges(self):
        print("Edges:")

        for u in range(self.size):
            for v in range(self.size):
                weight = self.matrix[u][v]
                if weight is not None:
                    print(f"Edge {chr(u + ord('A'))} --{weight}-> {chr(v + ord('A'))}")

    def __get_coordinate(self, vertex):
        if vertex >= 'a' and vertex <= 'z':
            position = ord(vertex) - ord('a')
        elif vertex >= 'A' and vertex <= 'Z':
            position = ord(vertex) - ord('A')
        else:
            raise ValueError("Vertex must be a letter")

        if position >= self.size:
            raise ValueError("The vertex does not exist in the graph")

        return position


graph = GraphMatrix(4)

graph.add_edge('A', 'B', 3)
graph.add_edge('A', 'D', 2)
graph.add_edge('B', 'A', 1)
graph.add_edge('B', 'C', 3)
graph.add_edge('B', 'D', 4)
graph.add_edge('C', 'B', 2)
graph.add_edge('C', 'D', 1)
graph.add_edge('D', 'C', 2)

graph.display_matrix()
graph.display_edges()
