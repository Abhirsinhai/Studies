from binarytree import tree
from binarytree import Node

root = Node(1)
root.left = Node(7)
root.left.left = Node(2)
root.left.right = Node(6)
root.left.right.left = Node(5)
root.left.right.right = Node(11)
root.right = Node(9)
root.right.right = Node(9)
root.right.right.left = Node(5)


print("Root postorder is:", root.postorder)
print("Root preorder is:", root.preorder)
print("Root inorder is:", root.inorder)


del(root)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)
root.right.left.right = Node(13)
root.right.right.left = Node(14)

print("Root postorder is:", root.postorder)
print("Root preorder is:", root.preorder)
print("Root inorder is:", root.inorder)