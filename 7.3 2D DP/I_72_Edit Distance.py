"""
References: https://www.youtube.com/watch?v=XYi2-LPrwm4
"""

from typing import List

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][n] = m - i
    
        for j in range(n + 1):
            dp[m][j] = n - j
        
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                # if same character, move both pointers
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                # add 1 for current operation
                # i, j + 1    : insert
                # i + 1, j    : delete
                # i + 1, j + 1: replace
                else:
                    dp[i][j] = 1 + min(dp[i][j+1], dp[i+1][j], dp[i+1][j+1])
        
        return dp[0][0]

mySol = Solution()
word1 = "horse"
word2 = "ros"
print(mySol.minDistance(word1, word2))