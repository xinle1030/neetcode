"""
References: https://www.youtube.com/watch?v=pNichitDD2E
"""

from typing import List
from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.count = 0 # use as timestamp
        self.tweetMap = defaultdict(list) # userId -> list of [count, tweetId]
        self.followMap = defaultdict(set) # userId -> set of followeeIds

    # Hashmap
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1 # decrement so we can get most recent posts with minHeap

    # Use minHeap with negative count numbers to get most recent posts, then merge k sorted list
    # O(k log k)
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId) # include own user Id

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                lastIdx = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][lastIdx]
                minHeap.append([count, tweetId, followeeId, lastIdx - 1]) # lastIdx - 1 is to point to next previous idx
        
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, lastIdx = heapq.heappop(minHeap)
            res.append(tweetId)

            # add next tweet
            if lastIdx >= 0:
                count, tweetId = self.tweetMap[followeeId][lastIdx]
                heapq.heappush(minHeap, [count, tweetId, followeeId, lastIdx - 1])

        return res

    # Use hashset to add in O(1)
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    # Use hashset to remove in O(1)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)