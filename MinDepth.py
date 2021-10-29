# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # dfs recursive
        
        if root is None: return 0
        
        children = [root.left, root.right]
        if None in children:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        
   def minDepth(self, root: Optional[TreeNode]) -> int:
    # dfs iterative
    # stack
    if root is None:
        return 0
    min_tracker = float('inf')
    stack = [[root, 1]]
    while stack:
        current = stack.pop()
        cur_node, cur_depth = current

        # Update min tracker if it is a leaf
        if cur_node.left is None and cur_node.right is None: # a leaf
            min_tracker = min(min_tracker, cur_depth)

        # left and right node
        if cur_node.left is not None: stack.append([cur_node.left, cur_depth + 1])
        if cur_node.right is not None: stack.append([cur_node.right, cur_depth + 1])

    return min_tracker
