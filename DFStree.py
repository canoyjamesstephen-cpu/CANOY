class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Preorder: Root -> Left -> Right
def preorder(node, result):
    if node is None:
        return
    result.append(node.data)
    preorder(node.left, result)
    preorder(node.right, result)


# Inorder: Left -> Root -> Right
def inorder(node, result):
    if node is None:
        return
    inorder(node.left, result)
    result.append(node.data)
    inorder(node.right, result)


# Postorder: Left -> Right -> Root
def postorder(node, result):
    if node is None:
        return
    postorder(node.left, result)
    postorder(node.right, result)
    result.append(node.data)


# Build the tree
#        C
#       / \
#      A   N
#     / \
#    O   Y
root = Node("C")
root.left = Node("A")
root.right = Node("N")
root.left.left = Node("O")
root.left.right = Node("Y")

# Run the traversals
pre, ino, post = [], [], []
preorder(root, pre)
inorder(root, ino)
postorder(root, post)

# Display the results
print("Name: CANOY")
print("DFS Methods in Tree\n")
print("Preorder  (Root-Left-Right):", " ".join(pre))
print("Inorder   (Left-Root-Right):", " ".join(ino))
print("Postorder (Left-Right-Root):", " ".join(post))