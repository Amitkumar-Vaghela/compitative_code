class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None 
        self.right = None 

def left_boundary(root): 
    if root: 
        if root.left: 
            print(root.data, end=" ") 
            left_boundary(root.left) 
        elif root.right: 
            print(root.data, end=" ") 
            left_boundary(root.right) 

def right_boundary(root): 
    if root: 
        if root.right: 
            right_boundary(root.right) 
            print(root.data, end=" ") 
        elif root.left: 
            right_boundary(root.left) 
            print(root.data, end=" ") 

def leaf_boundary(root): 
    if root: 
        leaf_boundary(root.left) 
        if root.left is None and root.right is None: 
            print(root.data, end=" ") 
        leaf_boundary(root.right) 

def print_boundary(root): 
    if root: 
        print(root.data, end=" ") 
        left_boundary(root.left) 
        leaf_boundary(root.left) 
        leaf_boundary(root.right) 
        right_boundary(root.right) 

# Create the binary tree
root = Node(1) 
root.left = Node(2) 
root.left.left = Node(3) 
root.left.right = Node(4) 
root.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 

print("Boundary order traversal of the binary tree:")
print_boundary(root)
