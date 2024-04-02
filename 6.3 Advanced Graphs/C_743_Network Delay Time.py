"""
References: https://www.youtube.com/watch?v=EaphyqKU4PQ

Dijkstra Shortest Path Algo: MinHeap (PathLength, Node) + BFS
Complexity = O(E log (V ^ 2)) = O(2E log V) = O(E log V)
"""

from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # create an adjacency list
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        visited = set() # keep track of visited nodes
        minHeap = [(0, k)] # append source node which has a path of 0
        t = 0 # maxTime
        
        while minHeap:
            w1, v1 = heapq.heappop(minHeap)
            
            if v1 not in visited:
                visited.add(v1)
                t = max(t, w1)

                for v2, w2 in edges[v1]:
                    if v2 not in visited:
                        heapq.heappush(minHeap, (w1 + w2, v2))
            
        return t if len(visited) == n else -1