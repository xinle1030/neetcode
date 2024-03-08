class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        return sorted_s == sorted_t

mySol = Solution()

s = "anagram"
t = "nagaram"
print(mySol.isAnagram(s, t))

s = "rat"
t = "car"
print(mySol.isAnagram(s, t))
