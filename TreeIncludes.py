# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_includes(root, target):
  # bfs iterative
  # queue
  # check for target once it leaves the queue
  
  if root is None: return False
  q = [root]
  while q:
    current = q.pop()
    if current.val == target:
      return True
    
    # left and right node
    if current.left is not None: q = [current.left] + q
    if current.right is not None: q = [current.right] + q
  return False
