"""
References: https://www.youtube.com/watch?v=Hr5cWUld4vU

DFS + DP (bottom up approach to find max sum in left and right subtree)
"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # could be negative so nid compare with 0 again
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute max path sum with split
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # this function dfs should return path sum without splitting
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]

mySol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(mySol.maxPathSum(root))

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(mySol.maxPathSum(root))