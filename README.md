# PT5-JARILLA-DAA-FINALS

This contains the following codes: 
#1. bubble_sort_steps.py
def bubble_sort_with_steps(arr):
    n = len(arr)
    round_num = 0

    print(f"Round {round_num}: {arr}")
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        round_num += 1
        print(f"Round {round_num}: {arr}")


data = [33, 41, 28, 15, 22, 10]


bubble_sort_with_steps(data)



# 2.A bfs_traversal.py
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



# 2.B in_order_traversal.py
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



#2.C pre_order_traversal.py
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




asciinema link: https://asciinema.org/a/0wP2rFI9u43jQrCHc94K6EjDo
