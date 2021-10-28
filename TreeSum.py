# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_sum(root):
  # dfs recursive
  if root is None: return 0
  
  left = tree_sum(root.left)
  right = tree_sum(root.right)
  return root.val + left + right
