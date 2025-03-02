matrix = [
    [0, 1, 0, 1],
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 0, 1, 0]]

print("Adjacency Matrix:")

for row in matrix:
    print(row)


print("Edges:")

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] == 1:
            print(f"Edge {i} -> {j}")
