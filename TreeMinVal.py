# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_min_value(root):
  # dfs recursive
  if root is None: return float('inf')
  # left and right node
  left = tree_min_value(root.left)
  right = tree_min_value(root.right)
  return min(root.val, left, right)v
