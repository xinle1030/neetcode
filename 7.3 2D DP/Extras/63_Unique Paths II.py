"""
References: https://www.youtube.com/watch?v=d3UOz7zdE4I&t=1s

Time Complexity: O(NM)
Space Complexity: O(N)
"""

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        dp = [0] * m

        # finish point is 1
        dp[-1] = 1

        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                # if obstacle is here
                if obstacleGrid[r][c]:
                    dp[c] = 0
                # within range
                elif c + 1 < m:
                    # go bottom or right
                    dp[c] = dp[c] + dp[c + 1]
        
        return dp[0]

mySol = Solution()
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(mySol.uniquePathsWithObstacles(obstacleGrid))

obstacleGrid = [[0,1],[0,0]]
print(mySol.uniquePathsWithObstacles(obstacleGrid))