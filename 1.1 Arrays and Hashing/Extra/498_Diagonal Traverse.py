"""
1. Diagonals are defined by the sum of indices in a 2 dimensional array
2. The snake phenomena can be achieved by reversing every other diagonal level, therefore check if divisible by 2
"""

from typing import List
from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                d[i + j].append(mat[i][j])
        
        ret = []

        for key, val in d.items():
            # if key is even, append in reverse order
            if key % 2 == 0:
                ret += val[::-1]
            else:
                ret += val
        
        return ret

mySol = Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(mySol.findDiagonalOrder(mat))

mat = [[1,2],[3,4]]
print(mySol.findDiagonalOrder(mat))