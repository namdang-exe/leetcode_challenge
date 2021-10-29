# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def max_path_sum(root):
  # dfs recursive
  
  # base cases
  if root is None: return float('-inf')
  if root.left is None and root.right is None: # a leaf
    return root.val
  
  # left and right node
  left = max_path_sum(root.left)
  right = max_path_sum(root.right)
  
  return root.val + max(left, right)
