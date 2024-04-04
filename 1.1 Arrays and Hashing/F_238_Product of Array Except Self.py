"""
References: https://www.youtube.com/watch?v=bNvIQI2wAjk

At the end of this pass, 
res[i] contains the product of all elements to the left of nums[i] multiplied by all elements to the right of nums[i]
, effectively excluding nums[i] itself.
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

mySol = Solution()
nums = [1,2,3,4]
print(mySol.productExceptSelf(nums))