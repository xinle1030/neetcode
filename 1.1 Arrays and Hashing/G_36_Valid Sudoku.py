"""
References: https://www.youtube.com/watch?v=TjFXEUCMqI8

Use HashSet for rows, columns and square -> O(9^2)
"""

from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set) # key = (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                # not a number
                if board[r][c] ==".":
                    continue
                
                # had seen this value at the (current row / current column / current square)
                if board[r][c] in rows[r] or \
                   board[r][c] in cols[c] or \
                   board[r][c] in squares[(r // 3, c // 3)]:
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        
        return True

