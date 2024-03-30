"""
References: https://www.youtube.com/watch?v=B1k_sxOSgv8

Use numberOfChars + delimiter as we will continue reading whatever is behind numberOfChars + delimiter until we reach the numberOfChars
Complexity: O(N), N = number of characters in the list

"""

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ""

        for string in strs:
            res += str(len(string)) + "#" + string
        
        return res

    def decode(self, str):
        """
        @param: str: A string
        @return: decodes a single string to a list of strings
        """
        res = []
        i = 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j]) # exclude character at j, which is #
            word = str[j + 1 : j + length + 1] # add 1 to skip #
            res.append(word)
            i = j + length + 1

        return res

mySol = Solution()
input = ['lint', 'code', 'love', 'you']
encodedStr = mySol.encode(input)
print(encodedStr)

decodedStr = mySol.decode(encodedStr)
print(decodedStr)