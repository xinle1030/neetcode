"""
References: https://www.youtube.com/watch?v=ihj4IQGZ2zc

1. root = preorder[0]
2. In inorder array, everything to the left of root = left subtree; everything to the right of root = right subtree
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(val = preorder[0])
        mid = inorder.index(preorder[0]) # find the index of the root val in inorder

        # preorder: 1:mid + 1 is the length of the elem in the left subtree
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid]) 
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root