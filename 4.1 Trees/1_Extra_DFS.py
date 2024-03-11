# References = https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/?ref=gcse

"""
Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
Auxiliary Space: O(V + E), since an extra visited array of size V is required, And stack size for iterative call to DFS function.
"""

from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.edges = defaultdict(list)
    
    def addEdge(self, u, v):
        self.edges[u].append(v)
    
    def dfs_util(self, visited, v, res):
        visited.add(v)
        res.append(v)

        for neighbour in self.edges[v]:
            if neighbour not in visited:
                self.dfs_util(visited, neighbour, res)

    def dfs(self, v):
        visited = set()
        res = []

        self.dfs_util(visited, v, res)

        return res

# Driver code
if __name__ == '__main__':
    # Create a graph given in the above diagram
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print(g.dfs(2))