# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_min_value(root):
  # dfs iterative
  # stack
  min_val = float('inf')
  stack = [root]
  while stack:
    current = stack.pop()
    min_val = min(min_val, current.val)
    
    # left and right node
    if current.left is not None: stack.append(current.left)
    if current.right is not None: stack.append(current.right)
  return min_val
    

# def tree_min_value(root):
#   # dfs recursive
#   if root is None: return float('inf')
#   # left and right node
#   left = tree_min_value(root.left)
#   right = tree_min_value(root.right)
#   return min(root.val, left, right)
