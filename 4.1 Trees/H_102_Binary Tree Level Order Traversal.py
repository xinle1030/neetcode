"""
References: https://leetcode.com/problems/binary-tree-level-order-traversal/solutions/4859313/level-order-traversal-of-binary-tree-using-breadth-first-search-bfs-in-c/

Traverse the binary tree level by level, also known as a breadth-first search (BFS) traversal.
"""

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []

        if not root:
            return ret
        
        q = deque()
        q.append(root)

        while q:
            temp = []
            for i in range(len(q)):
                popped_node = q.popleft()
                temp.append(popped_node.val)
                if popped_node.left: q.append(popped_node.left)
                if popped_node.right: q.append(popped_node.right)
            ret.append(temp)
        
        return ret
        
mySol = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(mySol.levelOrder(root))

root = TreeNode(1)
print(mySol.levelOrder(root))

root = None
print(mySol.levelOrder(root))
