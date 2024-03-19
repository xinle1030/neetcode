"""
References: https://www.youtube.com/watch?v=itmhHWaHupI

Use 2 heaps (small heap [max heap], large heap [min heap])
- add/remove : O(log n)
- get min/max : O(1)

Whenever push or remove from small heap, multiple the value by -1
Because to implement max heap, all elements need to be multiplied by 1 cuz python only implement min heap
"""

import heapq

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    # O(log n)
    def addNum(self, num: int) -> None:
        # by default, push to small heap
        heapq.heappush(self.small, -1 * num)

        # all elements in self.small <= in self.large
        if self.small and self.large and \
        (-1 * self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # handle uneven size (can only differ by 1)
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    # O(1)
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.small) == len(self.large):
            return (-1 * self.small[0] + self.large[0]) / 2
        else:
            return self.large[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()