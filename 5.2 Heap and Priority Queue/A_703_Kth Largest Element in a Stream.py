"""
References: https://www.youtube.com/watch?v=hOjcdrqMoQ8

Implementation: Min Heap of Size k to get the kth largest from the heap, which is at the min aka index 0
"""

from typing import List
import heapq

class KthLargest:

    # O(n log n)
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums

        heapq.heapify(self.minHeap) # using heapify to convert list into a min heap

        # need min heap of size k only to get kth largest from the heap
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0] # k largest element is at index 0 of minheap


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))   # return 4
print(kthLargest.add(5))   # return 5
print(kthLargest.add(10))  # return 5
print(kthLargest.add(9))   # return 8
print(kthLargest.add(4))   # return 8