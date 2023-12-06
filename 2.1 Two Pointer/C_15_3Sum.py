# References: https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        TARGET = 0

        if len(nums) < 3:
            return []

        my_nums = sorted(nums)

        ans = []

        for i in range(len(my_nums)):
            # elements are sorted in descending order, no more smaller elements behind to reduce to 0
            if my_nums[i] > 0:
                break

            # checks if the current element is a duplicate of the previous one (excluding the first element). 
            # If it is, the loop continues to the next element to avoid duplicate triplets.
            if i > 0 and my_nums[i] == my_nums[i - 1]:
                continue

            remaining = TARGET - my_nums[i]

            j = i + 1
            k = len(my_nums) - 1

            while j < k:
                if my_nums[j] + my_nums[k] == remaining:
                    ans.append([my_nums[i], my_nums[j], my_nums[k]])

                    # Handles duplicate values by advancing the pointers until they point to unique values.
                    lastLowOccurrence, lastHighOccurrence = my_nums[j], my_nums[k]

                    while j < k and lastLowOccurrence == my_nums[j]:
                        j += 1
                        
                    while j < k and lastHighOccurrence == my_nums[k]:
                        k -= 1
                        
                elif my_nums[j] + my_nums[k] > remaining:
                    k -= 1
                else:
                    j += 1
            
        return ans

mySol = Solution()
nums = [-1,0,1,2,-1,-4]
print(mySol.threeSum(nums))

nums = [0,1,1]
print(mySol.threeSum(nums))

nums = [0,0,0]
print(mySol.threeSum(nums))

nums = \
[34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]
print(mySol.threeSum(nums))