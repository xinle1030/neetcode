"""
References: https://www.youtube.com/watch?v=G8xtZy0fDKg
"""

from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        ret = []
        l = 0

        # make counters for beginning of string
        sCount = Counter(s[l:len(p)])
        pCount = Counter(p[l:len(p)])

        if sCount == pCount:
            ret.append(l)

        # sliding window for remaining string
        for r in range(len(p), len(s)):
            sCount[s[l]] -= 1

            # if count for current string == 0, pop it out
            if sCount[s[l]] == 0:
                sCount.pop(s[l])

            l += 1
            sCount[s[r]] += 1
            
            if sCount == pCount:
                ret.append(l)
        
        return ret

mySol = Solution()
s = "cbaebabacd"
p = "abc"
print(mySol.findAnagrams(s, p))

s = "abab"
p = "ab"
print(mySol.findAnagrams(s, p))