"""
References: https://www.youtube.com/watch?v=B7m8UmZE-vw

Create hashmap
char : lastIndex
"""

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdxMap = {}

        for i, char in enumerate(s):
            lastIdxMap[char] = i
        
        ret = []
        size, end = 0, 0

        for i, char in enumerate(s):
            size += 1
            lastIdx = lastIdxMap[char]

            end = max(end, lastIdx)

            # when reaching the end, meaning finish traverse characters in this partition, we can add the size
            if i == end:
                ret.append(size)
                size = 0
        
        return ret

mySol = Solution()
s = "ababcbacadefegdehijhklij"
print(mySol.partitionLabels(s))

s = "eccbbbbdec"
print(mySol.partitionLabels(s))