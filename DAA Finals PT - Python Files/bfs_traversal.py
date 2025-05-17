from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs_traversal(root):
    if not root:
        return []
    
    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

root = TreeNode('A')
root.left = TreeNode('C')
root.right = TreeNode('B')
root.right.left = TreeNode('E')
root.right.right = TreeNode('D')
root.right.right.right = TreeNode('F')

result = bfs_traversal(root)

print("BFS Traversal:", " – ".join(result))
