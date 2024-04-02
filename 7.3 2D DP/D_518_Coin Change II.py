"""
References: https://www.youtube.com/watch?v=Mjy4hd2xgrs

O(M * N), M = len(coins), N = amount
can be reduced to o(N)

number of rows: amount + 1
number of columns: coin + 1
"""

from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1) # to get amount 0, there is one way of combination, which is not taking any coin

        for val in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
                dp[val][i] = dp[val][i + 1] # look rightward
                if val - coins[i] >= 0:
                    dp[val][i] += dp[val - coins[i]][i] # look upward        
        return dp[amount][0]

mySol = Solution()
amount = 5
coins = [1,2,5]
print(mySol.change(amount, coins))