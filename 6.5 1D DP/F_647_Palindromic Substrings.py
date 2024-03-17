"""
References: https://www.youtube.com/watch?v=4RACzI5-du8
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):

            # odd length palindrome, expand from middle (single character) and compare character at both sides
            l = r = i
            res += self.countPalindromes(s, l, r)
            
            # even length palindrome, expand from middle (2 characters) and compare character at both sides
            l = i
            r = i + 1
            res += self.countPalindromes(s, l, r)
        
        return res
    
    def countPalindromes(self, s, l, r):
        count = 0

        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1

        return count

mySol = Solution()
s = "abc"
print(mySol.countSubstrings(s))

s = "aaa"
print(mySol.countSubstrings(s))