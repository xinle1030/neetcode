"""
References: https://www.youtube.com/watch?v=I7j0F7AHpb8
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy -> i + 1
        # sell -> i + 2 (need to have a cool down day)
        dp = {} # key = (i, buying) : val = maxProfit

        def dfs(i, buying):
            # go out of bounds, meaning cannot buy anymore
            if i >= len(prices):
                return 0
            
            # if ady computed, return value
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                # negate the boolean buying
                # if buy, need deduct the price
                buy = dfs(i + 1, not buying) - prices[i]
                cooldown = dfs(i + 1, buying) # no need negate 
                dp[(i, buying)] = max(buy, cooldown)
            else:
                # negate the boolean buying
                # if sell, get the profit
                sell = dfs(i + 2, not buying) + prices[i]
                cooldown = dfs(i + 1, buying) # no need negate 
                dp[(i, buying)] = max(sell, cooldown)
            
            return dp[(i, buying)]
        
        # at index 0, we must buy, which is the base case
        return dfs(0, True)