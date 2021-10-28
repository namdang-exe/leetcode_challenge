# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def depth_first_values(root):
  # dfs recursive
  if root is None: return []
  # a
  left = depth_first_values(root.left) # [b, d, e]
  right = depth_first_values(root.right) # [c,f]
  return [root.val] + left + right

# def depth_first_values(root):
#   # dfs iterative
#   # using stack
#   # last in first out
#   if root is None:
#     return []
#   result = []
#   stack = [root]
#   while stack:
#     current = stack.pop()
#     result.append(current.val)
    
#     # left and right node
#     if current.right is not None: stack += [current.right]
#     if current.left is not None: stack += [current.left]
    
#   return result


