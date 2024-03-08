from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                next_num = num + 1
                while next_num in nums_set:
                    next_num += 1
                max_len = max(max_len, next_num - num)
        
        return max_len

mySol = Solution()
nums = [100,4,200,1,3,2]
print(mySol.longestConsecutive(nums))

nums = [0,3,7,2,5,8,4,6,0,1]
print(mySol.longestConsecutive(nums))