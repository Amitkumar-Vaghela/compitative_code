class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_valid_BST(root, left=None, right=None):
    if root is None:
        return True
    
    if left is not None and root.data <= left.data:
        return False
    
    if right is not None and root.data >= right.data:
        return False
    
    return is_valid_BST(root.left, left, root) and is_valid_BST(root.right, root, right)

# Create the binary search tree
root = Node(10)
root.left = Node(8)
root.right = Node(19)
root.left.left = Node(5)
root.left.right = Node(9)

if is_valid_BST(root):
    print("The tree is a valid Binary Search Tree (BST).")
else:
    print("The tree is not a valid Binary Search Tree (BST).")
