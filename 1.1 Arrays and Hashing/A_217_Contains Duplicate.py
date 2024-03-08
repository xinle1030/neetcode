from typing import List
from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = defaultdict(int)

        for num in nums:
            if counter[num] > 0:
                return True
            else:
                counter[num] += 1
        
        return False

mySol = Solution()

nums = [1,2,3,1]
print(mySol.containsDuplicate(nums))

nums = [1,2,3,4]
print(mySol.containsDuplicate(nums))

nums = [1,1,1,3,3,4,3,2,4,2]
print(mySol.containsDuplicate(nums))
