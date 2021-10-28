# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_sum(root):
  # dfs iterative
  # stack

  if root is None: return 0
  total = 0
  stack = [root]
  while stack:
    current = stack.pop()
    total += current.val
    
    # left and right node
    if current.left is not None: stack.append(current.left)
    if current.right is not None: stack.append(current.right)
    
  return total

# def tree_sum(root):
#   # dfs recursive
#   if root is None: return 0
  
#   left = tree_sum(root.left)
#   right = tree_sum(root.right)
#   return root.val + left + right
