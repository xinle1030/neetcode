"""
References: https://www.youtube.com/watch?v=s8p8ukTyA2I

1. Processing most frequent elements will give less idle time
2. Implement maxheap to keep track of the frequent characters -> O(26) due to 26 characters
3. Need another queue, where each element = (frequency left, next time available)
4. Complexity = O(N * M), where N = number of tasks, M = number of idle time
"""

from typing import List
import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxHeap = [-1 * count for count in counter.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0

        # while maxHeap and q are not empty
        while maxHeap or q:
            time += 1

            # if maxHeap is not empty
            if maxHeap:
                # add on count
                count = 1 + heapq.heappop(maxHeap)
                # if count is non-zero (check <0 because we implementing maxHeap)
                if count < 0:
                    q.append([count, time + n])

            # if q is not empty and if it is now the time to add back the task
            if q and q[0][1] == time:
                countInQueue = q.popleft()[0]
                heapq.heappush(maxHeap, countInQueue)
        
        return time

mySol = Solution()

tasks = ["A","A","A","B","B","B"]
n = 2
print(mySol.leastInterval(tasks, n))

tasks = ["A","C","A","B","D","B"]
n = 1
print(mySol.leastInterval(tasks, n))

tasks = ["A","A","A", "B","B","B"]
n = 3
print(mySol.leastInterval(tasks, n))