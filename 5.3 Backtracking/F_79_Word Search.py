"""
References: https://www.youtube.com/watch?v=pfiQ_PS1g8E

Time Complexity: O(r * c * 4 ^ p), where p = len(word)

- 4 because we call dfs 4 times to traverse to 4 different directions
"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        # keep track of the traverse path, so we dont traverse through the same point twice
        path = set()

        # i: curr character index
        def dfs(r, c, i):
            # found all the words dy
            if i == len(word):
                return True
            # out of bound | traverse to the same point again | current character is wrong
            elif (r < 0 or c < 0 or r > ROWS - 1 or c > COLS - 1) or \
                 ((r, c) in path) or \
                 word[i] != board[r][c]:
                return False
            
            # Marking Visited Cells: Before entering a cell (r, c) during the DFS, the code adds (r, c) to the path set to mark it as visited. 
            # This prevents revisiting the same cell again during the current traversal path.
            path.add((r, c))

            # travel to all four directions
            res =   dfs(r + 1, c, i + 1) or \
                    dfs(r, c + 1, i + 1) or \
                    dfs(r - 1, c, i + 1) or \
                    dfs(r, c - 1, i + 1)
            
            # Backtracking: After exploring all possible paths from the current cell (r, c), regardless of whether the word is found or not, it's crucial to backtrack by removing (r, c) from the path set. 
            # This ensures that the cell is not marked as visited when exploring different paths from other cells later in the search process.
            path.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): 
                    return True
        
        return False
            
mySol = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(mySol.exist(board, word))

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] 
word = "SEE"
print(mySol.exist(board, word))

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(mySol.exist(board, word))