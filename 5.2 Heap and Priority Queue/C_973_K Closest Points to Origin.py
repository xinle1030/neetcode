from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.minHeap = []
        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            self.minHeap.append((distance, point))
        heapq.heapify(self.minHeap)

        smallest = heapq.nsmallest(k, self.minHeap)
        ret = [value for key, value in smallest]
        
        return ret

mySol = Solution()
points = [[3,3],[5,-1],[-2,4]]
k = 2

print(mySol.kClosest(points, k))