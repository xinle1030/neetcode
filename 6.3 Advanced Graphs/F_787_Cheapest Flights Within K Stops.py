"""
References: https://www.youtube.com/watch?v=5eIK3zUdYmE

Bellman-Ford Algo: O(E * k), where k = number of stops
- uses BFS
- can deal with negative weights
- run for each edge loop for (k + 1) times
"""

from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0 # price to reach src node = 0

        # run for k + 1 times
        for i in range(k + 1):
            tempPrices = prices.copy() # temp arr for updating value

            # loop for each edge in flights
            for s, d, p in flights: # s = source, d = dest, p = price
                # not reachable
                if prices[s] == float('inf'):
                    continue
                # found shorter path from src to dest
                if prices[s] + p < tempPrices[d]:
                    tempPrices[d] = prices[s] + p
            prices = tempPrices
        
        if prices[dst] == float('inf'):
            return -1
        else:
            return prices[dst]