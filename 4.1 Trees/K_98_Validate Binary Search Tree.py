from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Method 1: With a helper function
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = [None]  # Use a list to make prev mutable
        return self.isBST(root, prev)

    def isBST(self, root: Optional[TreeNode], prev: List[TreeNode]) -> bool:
        if not root:
            return True
        left = self.isBST(root.left, prev)

        if prev[0] and prev[0].val >= root.val:
            return False
        
        prev[0] = root

        right = self.isBST(root.right, prev)

        return left and right
    
    """
    Method 2: Define in __init__
    """
    def __init__(self) -> None:
        self.prev = None
    
    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        # Base case: Empty tree is a valid BST
        if not root:
            return True
        
        left = self.isValidBST2(root.left)

        # Check if current node violates BST property
        if self.prev and self.prev.val >= root.val:
            return False
        
        # Update prev
        self.prev = root

        right = self.isValidBST2(root.right)

        return left and right

mySol = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(mySol.isValidBST2(root))

root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(mySol.isValidBST2(root))

root = TreeNode(1)
root.left = TreeNode(1)
print(mySol.isValidBST2(root))