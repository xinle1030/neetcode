from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        elif len(cost) == 1:
            return cost[0]
        elif len(cost) == 2:
            return min(cost)

        dp = [-1] * len(cost)

        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        return min(dp[-1], dp[-2])

mySol = Solution()
cost = [10,15,20]
print(mySol.minCostClimbingStairs(cost))

cost = [1,100,1,1,1,100,1,1,100,1]
print(mySol.minCostClimbingStairs(cost))