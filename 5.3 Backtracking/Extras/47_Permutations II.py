from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * len(nums)

        permutation = []

        def backtrack():
            if len(permutation) == len(nums):
                res.append(permutation[:])
                return
            else:
                # no nid pop from used as it will be reset for each call stack
                used = set()
                for i in range(len(nums)):
                    if not visited[i] and nums[i] not in used:
                        visited[i] = True
                        permutation.append(nums[i])
                        used.add(nums[i])

                        backtrack()

                        visited[i] = False
                        permutation.pop()
         
        backtrack()
        return res


mySol = Solution()
nums = [1,1,2]
print(mySol.permuteUnique(nums))

nums = [1,2,3]
print(mySol.permuteUnique(nums))