"""
Reference: https://www.geeksforgeeks.org/preorder-traversal-of-binary-tree/
"""

# Structure of a Binary Tree Node
class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

def printPreorder(root):
    if root == None:
        return
    
    print(root.data, end=' ')

    printPreorder(root.left)

    printPreorder(root.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    # Function call
    print("Preorder traversal of binary tree is:")
    printPreorder(root)