from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxHeap = [-1 * x for x in stones]
        heapq.heapify(self.maxHeap)
        length = len(self.maxHeap)

        while len(self.maxHeap) > 1:
            y = -1 * heapq.heappop(self.maxHeap)
            x = -1 * heapq.heappop(self.maxHeap)

            if x != y:
                newVal = y - x
                heapq.heappush(self.maxHeap, -1 * newVal)
        
        if len(self.maxHeap) > 0:
            return -1 * self.maxHeap[0]
        else:
            return 0

mySol = Solution()
stones = [2,7,4,1,8,1]

print(mySol.lastStoneWeight(stones))

