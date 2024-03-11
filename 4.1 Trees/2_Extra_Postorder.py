"""
Reference: https://www.geeksforgeeks.org/postorder-traversal-of-binary-tree/
"""

# Structure of a Binary Tree Node
class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

def printPostorder(root):
    if root == None:
        return
    
    printPostorder(root.left)

    printPostorder(root.right)

    print(root.data, end=' ')
    

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    # Function call
    print("Postorder traversal of binary tree is:")
    printPostorder(root)