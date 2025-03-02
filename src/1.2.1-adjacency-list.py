adjacency_list = [
    [1, 3],
    [0, 2, 3],
    [1, 3],
    [2]]


print("Edges:")

for i in range(len(adjacency_list)):
    for j in range(len(adjacency_list[i])):
        print(f"Edge {i} -> {adjacency_list[i][j]}")
