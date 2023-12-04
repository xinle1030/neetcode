from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        buyIdx = 0
        sellIdx = 1
        profit = 0

        while sellIdx < len(prices):

            tempProfit = prices[sellIdx] - prices[buyIdx]
            if prices[sellIdx] > prices[buyIdx]:
                profit = max(profit, tempProfit)
            # if there is a day with a price lower than my buy price, set my buy price to this
            else:
                buyIdx = sellIdx
            
            sellIdx += 1

        return profit

    
mySol = Solution()
prices = [7,1,5,3,6,4]
print(mySol.maxProfit(prices))

prices = [7,6,4,3,1]
print(mySol.maxProfit(prices))