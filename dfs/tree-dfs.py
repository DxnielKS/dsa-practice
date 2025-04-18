from typing import Optional

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root):
    """DFS traversal of the tree rooted at root."""
    if root is None:
        return
    
    print(f"Current traversal value: {root.val}")

    dfs(root.left)
    dfs(root.right)


# TEST CASE
root = Node(1)
node1 =  Node(2)
node3 = Node(3)
node4 = Node(4)

root.left = node1
node1.left = node4
root.right = node3

dfs(root)