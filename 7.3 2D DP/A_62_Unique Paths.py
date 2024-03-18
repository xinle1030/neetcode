"""
References: https://www.youtube.com/watch?v=IlEsdxuD4lY

Build row by row from bottom row
"""

class Solution:
    # m: number of rows
    # n: number of columns
    def uniquePaths(self, m: int, n: int) -> int:
        baseRow = [1] * n

        # do for (m - 1) of rows, as last row is always 1s
        for i in range(m - 1):
            newRow = [1] * n
            # exclude last column which is always 1, iterate from left to right
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + baseRow[j]
            baseRow = newRow
        
        # answer will be stored at first index in baseRow which is the starting point
        return baseRow[0]
    
mySol = Solution()
m = 3
n = 7
print(mySol.uniquePaths(m, n))

m = 3
n = 2
print(mySol.uniquePaths(m, n))