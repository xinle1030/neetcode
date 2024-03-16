"""
Reference: https://www.geeksforgeeks.org/inorder-traversal-of-binary-tree/
"""

# Structure of a Binary Tree Node
class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

def printInorder(root):
    if root == None:
        return
    
    printInorder(root.left)

    print(root.data, end=' ')

    printInorder(root.right)
    

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    # Function call
    print("Inorder traversal of binary tree is:")
    printInorder(root)

    print()

    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)

    # Function call
    print("Inorder traversal of binary tree is:")
    printInorder(root)