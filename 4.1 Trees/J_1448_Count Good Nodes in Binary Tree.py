"""
References: https://www.youtube.com/watch?v=7cp5imvDzl4

Time Complexity = O(n), n = number of nodes
Space Complexity = O(log n), log n = height of trees

Use Preorder traversal
Root node is a good node
Formula = 1 + left + right, where 1 refers to root node
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if not node:
                return 0
            
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val) # update the max value u have seen so far

            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        
        return dfs(root, root.val)