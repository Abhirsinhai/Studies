from binarytree import tree
from binarytree import Node
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')
root.right.right = Node('G')
root.left.right.right = Node('H')
root.right.left.right = Node('I')
root.right.left.right.right = Node('J')

print("Root postorder is:", root.postorder)
print("Root preorder is:", root.preorder)
print("Root inorder is:", root.inorder)