# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_includes(root, target):
  # dfs recursive
  if root is None: return False
  if root.val == target: return True
  left = tree_includes(root.left, target) # boolean
  right = tree_includes(root.right, target) # boolean
  return (left or right)
  

# def tree_includes(root, target):
#   # bfs iterative
#   # queue
#   # check for target once it leaves the queue
  
#   if root is None: return False
#   q = [root]
#   while q:
#     current = q.pop()
#     if current.val == target:
#       return True
    
#     # left and right node
#     if current.left is not None: q = [current.left] + q
#     if current.right is not None: q = [current.right] + q
#   return False

  
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

tree_includes(a, "e") # -> True
