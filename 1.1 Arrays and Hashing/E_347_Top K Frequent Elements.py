"""
References: https://www.youtube.com/watch?v=YPTqKIgVk-k

Maintain maxHeap of size k -> O(k log N)
Use bucket sort -> O(N)
"""

from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = [[] for i in range(len(nums) + 1)]
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        
        # use count as the index instead as the freq array is bounded by size of input array
        for num, count in counter.items():
            freq[count].append(num)
        
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

mySol = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(mySol.topKFrequent(nums, k))

nums = [1]
k = 1
print(mySol.topKFrequent(nums, k))

nums = [1, 2]
k = 2
print(mySol.topKFrequent(nums, k))