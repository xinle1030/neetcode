"""
References: https://www.youtube.com/watch?v=vRbbcKXCxOw

Recursive DFS
O(p + q) = O(size of both trees) as worst case is that we have to iterate every single nodes
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 3 base cases
        if not p and not q:
            return True
        if not p or not q: # one of them is null
            return False
        if p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right