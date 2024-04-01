"""
Reference: https://www.youtube.com/watch?v=lXVy6YWFcRM

Keep track of min and max because of negative * negative = positive
If encounter 0, take it as 1 
"""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin, currMax = 1, 1

        for n in nums:

            # keep it as one and skip
            if n == 0:
                currMin, currMax = 1, 1
                continue

            temp1 = n * currMin
            temp2 = n * currMax

            currMin = min(temp1, temp2, n)
            currMax = max(temp1, temp2, n)
            
            res = max(res, currMax)

        return res

mySol = Solution()
nums = [2,3,-2,4]
print(mySol.maxProduct(nums))

nums = [-2,0,-1]
print(mySol.maxProduct(nums))

nums = [0, 2]
print(mySol.maxProduct(nums))

nums = [-2,3,-4]
print(mySol.maxProduct(nums))