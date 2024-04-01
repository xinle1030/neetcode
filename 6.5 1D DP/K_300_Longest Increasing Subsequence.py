"""
References: https://www.youtube.com/watch?v=cjWnW0hdF1Y

Work from end of list, which is the base case = 1
Then check remaining index j from current idx i
Complexity: O(n^2)
"""

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        # work from backwards
        for i in range(len(nums) - 1, -1, -1):
            # check remaining index j from current idx i 
            for j in range(i + 1, len(nums)):

                # if is in increasing order, update dp[i]
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)

mySol = Solution()
nums =[4,10,4,3,8,9]
print(mySol.lengthOfLIS(nums))

nums = [10,9,2,5,3,7,101,18]
print(mySol.lengthOfLIS(nums))

nums = [0,1,0,3,2,3]
print(mySol.lengthOfLIS(nums))

nums = [7,7,7,7,7,7,7]
print(mySol.lengthOfLIS(nums))