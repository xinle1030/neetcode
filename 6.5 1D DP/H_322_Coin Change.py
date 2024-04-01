"""
Reference: Monash Y2S2 Week 4 Lecture 04: DP Pg 79 - 141

Time Complexity = O(Amount * len(coins))
Space Complexity = O(Amount)
"""

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        dp = [ float('inf') ] * (amount + 1)
        dp[0] = 0

        for value in range(1, len(dp)):
            for coin in coins:
                if coin <= value:
                    balance = value - coin
                    count = 1 + dp[balance] # find dp[balance] to add up to the balance amount
                    dp[value] = min(dp[value], count)
        
        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]

mySol = Solution()
coins = [1,2,5]
amount = 11
print(mySol.coinChange(coins, amount))

coins = [2]
amount = 3
print(mySol.coinChange(coins, amount))

coins = [1]
amount = 0
print(mySol.coinChange(coins, amount))