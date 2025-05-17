class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def in_order_traversal(node, result):
    if node:
        in_order_traversal(node.left, result)
        result.append(node.value)
        in_order_traversal(node.right, result)


root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('D')
root.left.left = TreeNode('C')
root.right.left = TreeNode('E')
root.right.right = TreeNode('F')

result = []
in_order_traversal(root, result)

print("In-order Traversal:", " – ".join(result))
