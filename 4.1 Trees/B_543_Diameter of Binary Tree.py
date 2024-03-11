"""
References: https://www.youtube.com/watch?v=bkxqA8Rfv04
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # using a mutable object like a list to store and update the value is a valid way to address the scoping issue in this particular scenario. 
        # It allows you to effectively update the value within the function and retrieve it outside the function.
        res = [0]

        def dfs(root):
            if not root:
                return -1 
            
            lheight = dfs(root.left)
            rheight = dfs(root.right)

            # update the diameter of the current traversing node = 2 + left + right [plus 2 is because of two new edges to left and right]
            res[0] = max(res[0], 2 + lheight + rheight)

            return 1 + max(lheight, rheight) # get the height of the current node
        
        dfs(root)

        return res[0]

mySol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(mySol.diameterOfBinaryTree(root))