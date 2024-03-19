"""
References: https://www.youtube.com/watch?v=s7AvT7cGdSo
"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        permutation = []
        def backtrack():
            if len(permutation) == len(nums):
                res.append(permutation.copy())
            else:
                for i in range(len(nums)):
                    if nums[i] in permutation: continue
                    permutation.append(nums[i])
                    backtrack()
                    permutation.pop()
        
        backtrack()
        return res

mySol = Solution()
nums = [1,2,3]
print(mySol.permute(nums))

nums = [0,1]
print(mySol.permute(nums))

nums = [1]
print(mySol.permute(nums))

