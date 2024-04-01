"""
References: https://www.youtube.com/watch?v=73r3KWiEvyk
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n + 1, ...]
        for n in nums:
            temp = max(rob1 + n, rob2) # whether to include current element or not
            rob1 = rob2 # move forward
            rob2 = temp # update to newly computed val
        
        return rob2

    def rob2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [-1] * len(nums)
        dp[0], dp[1], dp[2] = nums[0], nums[1], dp[2]

        for i in range(2, len(nums)):
            dp[i] = nums[i] + max(dp[i - 2], dp[i - 3])
        
        return max(dp[-1], dp[-2])

mySol = Solution()
nums = [1,2,3,1]
print(mySol.rob(nums))

nums = [2,7,9,3,1]
print(mySol.rob(nums))

nums = [2,1,1,2]
print(mySol.rob(nums))