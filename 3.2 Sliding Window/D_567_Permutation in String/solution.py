class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26

        if len(s2) < len(s1):
            return False
        
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        
        j = 0
        k = len(s1) - 1

        while k < len(s2):
            if count1 == count2:
                return True
            else:
                # reduce leaving char count
                count2[ord(s2[j]) - ord('a')] -= 1
                j += 1
                k += 1

                if k < len(s2):
                    # increase introduced char count
                    count2[ord(s2[k]) - ord('a')] += 1

        return False

mySol = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(mySol.checkInclusion(s1, s2))

s1 = "ab"
s2 = "eidboaoo"
print(mySol.checkInclusion(s1, s2))