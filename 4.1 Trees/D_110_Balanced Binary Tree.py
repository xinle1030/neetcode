"""
A balanced binary tree or height-balanced binary tree is such a tree whose left and right subtrees' heights differ by not more than 1, 
which means the height difference could be -1, 0, and 1. 

A balanced binary tree is also known as a height-balanced tree.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                # return [isBalanced, height of the tree]
                return [True, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)

            differenceInHeights = abs(left[1] - right[1])

            balanced = left[0] and right[0] and differenceInHeights <= 1

            # height of the tree = max(lHeight, rHeight) + 1
            return [balanced, max(left[1], right[1]) + 1]
        
        result = dfs(root)

        return result[0]

mySol = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(mySol.isBalanced(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)
print(mySol.isBalanced(root))

root = None
print(mySol.isBalanced(root))