# Algorithms and Data Structures - Graphs


## Graphs Representation

### Adjacency Matrix

#### Asymptotic Complexity
- Time complexity:
  - Insertion: O(1)
  - Deletion: O(1)
- Space complexity: O(V^2)

#### Pros
- Simple to implement
- Fast to access edge (u, v), O(1), fast to add and remove edges

#### Cons
- Space complexity is O(V^2)
- Its not efficient for sparse graphs

#### Demos
- [Adjacency Matrix](./src/1.1.1-adjacency-matrix.py)
- [Undirected Graph](./src/1.1.2-undirected-graph-matrix.py)
- [Directed Graph](./src/1.1.3-directed-graph-matrix.py)
- [Adjacency Matrix - Playground](./src/1.1.4-adjacency-matrix-playground.py)


### Adjacency List

#### Demos
  - [Adjacency List](./src/1.2.1-adjacency-list-with-list.py)
  - [Adjacency List Weighted](./src/1.2.2-adjacency-list-weighted.py)


## References
- [Other Algorithms & Data Structures](https://github.com/NelsonBN/algorithms-data-structures)
