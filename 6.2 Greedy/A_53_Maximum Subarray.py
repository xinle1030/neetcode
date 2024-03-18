"""
References: https://www.youtube.com/watch?v=5WZl3MMT0Eg

Kadane's algorithm: https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0

        for num in nums:
            # if become negative, reset to 0
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSum = max(maxSum, currSum)
        
        return maxSum

mySol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(mySol.maxSubArray(nums))

nums = [1]
print(mySol.maxSubArray(nums))

nums = [5,4,-1,7,8]
print(mySol.maxSubArray(nums))