class GraphMatrix:
    def __init__(self, size):
        self.matrix = [[0] * size for _ in range(size)]
        self.size = size

    def add_edge(self, u, v):
        position_u = self.__get_coordinate(u)
        position_v = self.__get_coordinate(v)

        if position_u == position_v:
            raise ValueError("The edge must not be a loop")

        self.matrix[position_u][position_v] = 1
        self.matrix[position_v][position_u] = 1

    def remove_edge(self, u, v):
        position_u = self.__get_coordinate(u)
        position_v = self.__get_coordinate(v)

        if position_u == position_v:
            raise ValueError("The edge must not be a loop")

        self.matrix[position_u][position_v] = 0
        self.matrix[position_v][position_u] = 0

    def display_matrix(self):
        print("Adjacency Matrix:")

        print(" ", end=" ")
        for i in range(self.size):
            print(chr(i + ord('A')), end=" ")

        print()
        for i in range(self.size):
            print(chr(i + ord('A')), end=" ")
            for j in range(self.size):
                print(self.matrix[i][j], end=" ")
            print()

    def display_edges(self):
        """
        This matrix is symmetric, so we only need to display the upper triangle and we can ignore the diagonal because the graph does not support edge to itself.
        """
        print("Edges:")

        v_total = 1
        for u in range(1, self.size):
            for v in range(v_total):
                if self.matrix[u][v] == 1:
                    print(f"Edge {chr(u + ord('A'))} <-> {chr(v + ord('A'))}")
            v_total = v_total + 1

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

graph.add_edge('A', 'B') # (0, 1)
graph.add_edge('B', 'C') # (1, 2)
graph.add_edge('C', 'D') # (2, 3)
graph.add_edge('D', 'A') # (3, 0)

graph.display_matrix()
graph.display_edges()
