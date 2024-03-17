"""
References: https://www.youtube.com/watch?v=Ua0GhsJSlWM

Bottom Up 2D DP
Time / Space Complexity = O(N * M), where N = len(text1), M = len(text2)

If the current character matches, go diagonally to match the remaining substring -> 1 + diagonal
Else, go right or down to see check if next character matches -> 0 + max(right, down)
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # add extra column and row to dp matrix
        dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) -1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]