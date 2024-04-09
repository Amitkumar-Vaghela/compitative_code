class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if not root:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    if data > root.data:
        root.right = insert(root.right, data)
    return root

def inorder(root, result=[]):
    if root:
        inorder(root.left, result)
        result.append(root.data)
        inorder(root.right, result)
    return result

def is_bst(root):
    in_order_list = inorder(root)
    return in_order_list == sorted(in_order_list)

# Create the binary search tree
root = None
keys = [8, 3, 1, 6, 4, 7, 10, 14, 13]

for key in keys:
    root = insert(root, key)

print("Inorder traversal of the BST:", inorder(root))

if is_bst(root):
    print("The tree is a Binary Search Tree (BST).")
else:
    print("The tree is not a Binary Search Tree (BST).")
