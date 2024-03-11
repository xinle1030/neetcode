# References = https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
"""
Time Complexity: O(V+E), where V is the number of nodes and E is the number of edges.
Auxiliary Space: O(V)
"""

from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.edges = defaultdict(list)
    
    def addEdge(self, u, v):
        self.edges[u].append(v)
    
    def bfs(self, s):
        queue = []
        visited = [False] * (len(self.edges))

        queue.append(s)
        visited[s] = True
        res = []

        while len(queue) > 0:
            s = queue.pop(0)
            res.append(s)

            for i in self.edges[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        
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

    print(g.bfs(2))

