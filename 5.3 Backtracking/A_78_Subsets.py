"""
References: https://www.youtube.com/watch?v=REOH22Xwdkk

Time Complexity: O(n x 2^n)
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            # base case
            if i >= len(nums):
                res.append(subset.copy())
                return 
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision not to include nums[i]
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res

mySol = Solution()
nums = [1,2,3]
print(mySol.subsets(nums))

nums = [0]
print(mySol.subsets(nums))