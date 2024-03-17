# https://leetcode.ca/all/340.html

from collections import defaultdict 

"""
Question:
Given a string s, find the length of the longest substring T that contains at most k distinct characters.

Example:
For example, Given s = "eceba", k = 3,
T is "eceb" which its length is 4.

Challenge:
O(n), n is the size of the string s.
"""

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        charMap = defaultdict(int)
        maxLen = 0
        j = 0
        
        # i is the right pointer
        for i in range(len(s)):
            char_i = s[i]
            charMap[char_i] += 1

            # j is the left pointer
            # remove character from charMap when number of distinct character exceeds k
            while len(charMap) > k:
                char_j = s[j]
                charMap[char_j] -= 1

                # distinct character no longer exists in the charMap
                if charMap[char_j] == 0:
                    del charMap[char_j]

                j += 1
            
            maxLen = max(maxLen, i - j + 1)
            
        return maxLen
            
mySol = Solution()
s = "eceba"
k = 2
print(mySol.lengthOfLongestSubstringKDistinct(s, k)) # T is "ece" which its length is 3.

s = "eceba"
k = 3
print(mySol.lengthOfLongestSubstringKDistinct(s, k)) # T is "eceb" which its length is 4.

s = "aa"
k = 1
print(mySol.lengthOfLongestSubstringKDistinct(s, k)) # T is "aa" which its length is 2.