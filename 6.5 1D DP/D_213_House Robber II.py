"""
References: https://www.youtube.com/watch?v=rWAJCfYYOvM

Reuse House Robber solution on arr[1:n - 1] and on [2:n] respectively
"""

from typing import List

class Solution:
    def rob_aux(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
    
    def rob(self, nums: List[int]) -> int:

        arr1 = nums[1:] # exclude first elem
        arr2 = nums[:-1] # exclude last elem

        # include nums[0] if len(nums) == 1
        return max(nums[0], self.rob_aux(arr1), self.rob_aux(arr2))

mySol = Solution()
nums = [2,3,2]
print(mySol.rob(nums))

nums = [1,2,3,1]
print(mySol.rob(nums))

nums = [1,2,3]
print(mySol.rob(nums))