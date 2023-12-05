# References: https://aaronice.gitbook.io/lintcode/two_pointers/longest-repeating-character-replacement

"""
maxCount may be invalid at some points, but this doesn't matter, because it was valid earlier in the string, 
and all that matters is finding the max window that occurred anywhere in the string. 

Additionally, it will expand _if and only if _enough repeating characters appear in the window to make it expand. 
So whenever it expands, it's a valid expansion.
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charIndices = [0] * 26 # for upper case letter only
        maxLen = 0
        maxCount = 0

        j = 0 # left pointer

        # right pointer
        for i in range(len(s)):
            char_i = s[i]
            right_idx = ord(char_i) - ord('A')
            charIndices[right_idx] += 1
            
            # largest number of repeating characters
            maxCount = max(maxCount, charIndices[right_idx])

            # window size = i - j + 1
            # i - j + 1 - maxCount = number of characters need to replace within a window
            # number of characters need to replace within a window > k
            while i - j + 1 - maxCount > k:
                char_j = s[j]
                left_idx = ord(char_j) - ord('A')

                charIndices[left_idx] -= 1
                j += 1  # move left pointer
            
            maxLen = max(maxLen, i - j + 1)
        
        return maxLen

mySol = Solution()
s = "ABAB" 
k = 2
print(mySol.characterReplacement(s, k))

s = "AABABBA" 
k = 1
print(mySol.characterReplacement(s, k))