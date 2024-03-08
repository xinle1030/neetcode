from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = defaultdict(list)
        
        for i in range(len(strs)):
            curr = strs[i]

            sorted_word = ''.join(sorted(curr))
            counter[sorted_word].append(curr)
        
        return list(counter.values())

mySol = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]
print(mySol.groupAnagrams(strs))

strs = [""]
print(mySol.groupAnagrams(strs))

strs = ["a"]
print(mySol.groupAnagrams(strs))