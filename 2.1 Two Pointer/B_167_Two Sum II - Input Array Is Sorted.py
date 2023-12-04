from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
                
        while i < j:
             if numbers[i] + numbers[j] == target:
                 return [i + 1, j + 1]
             elif numbers[i] + numbers[j] > target:
                 j -= 1
             else:
                 i += 1

    
mySol = Solution()
numbers = [2,7,11,15]
target = 9
print(mySol.twoSum(numbers, target))

numbers = [2,3,4]
target = 6
print(mySol.twoSum(numbers, target))

numbers = [-1,0]
target = -1
print(mySol.twoSum(numbers, target))

numbers = [-3,3,4,90]
target = 0
print(mySol.twoSum(numbers, target))