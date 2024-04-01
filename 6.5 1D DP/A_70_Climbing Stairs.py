"""
References: https://youtube.com/watch?v=Y0lT9Fck7qI

Like fibonacci
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        base1, base2 = 1, 1

        for i in range(n - 1):
            temp = base1
            base1 = base1 + base2
            base2 = temp
        
        return base1

mySol = Solution()
n = 2
print(mySol.climbStairs(n))

n = 3
print(mySol.climbStairs(n))