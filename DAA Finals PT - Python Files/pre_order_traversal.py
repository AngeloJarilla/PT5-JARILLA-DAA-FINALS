class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def pre_order_traversal(node, result):
    if node:
        result.append(node.value)
        pre_order_traversal(node.left, result)
        pre_order_traversal(node.right, result)

root = TreeNode('A')
root.left = TreeNode('F')
root.right = TreeNode('B')
root.left.left = TreeNode('G')
root.right.left = TreeNode('C')
root.right.right = TreeNode('D')
root.right.left.right = TreeNode('E')

result = []
pre_order_traversal(root, result)

print("Pre-order Traversal:", " – ".join(result))
