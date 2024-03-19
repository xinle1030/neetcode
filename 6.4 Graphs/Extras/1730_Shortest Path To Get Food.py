"""
References: https://www.youtube.com/watch?v=bY4I3pCZLTg

Use BFS, but not DFS because Shortest Path Guarantee
- BFS guarantees that the first time a node is visited, it is reached via the shortest path from the start node. 
- This property ensures that when you find the food node, you have indeed found the shortest path to it.

DFS can also be used to find paths in a grid, BFS is generally preferred when the goal is to find the shortest path.
"""
from typing import List
from collections import deque

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        q = deque()

        # find starting point *
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "*":
                    visited.add((row, col))
                    q.append((row, col, 0))

                    break
        
        # move up down, left right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while q:
            currRow, currCol, steps = q.popleft()
            # found food position #
            if grid[currRow][currCol] == "#":
                return steps
            else:
                for horizontal, vertical in directions:
                    newRow = currRow + horizontal
                    newCol = currCol + vertical

                    if 0 <= newRow < ROWS and 0 <= newCol < COLS \
                    and grid[newRow][newCol] != "X":

                        if (newRow, newCol) not in visited:
                            visited.add((newRow, newCol))
                            q.append((newRow, newCol, steps + 1))
        
        return -1
    
mySol = Solution()
grid = [
    ["X", "X", "X", "X", "X", "X"],
    ["X", "*", "O", "O", "O", "X"],
    ["X", "O", "O", "#", "O", "X"],
    ["X", "X", "X", "X", "X", "X"],
]
print(mySol.getFood(grid))