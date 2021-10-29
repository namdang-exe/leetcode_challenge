# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # dfs recursive
        
        # base case
        if root is None: return 0
        if root.left is None and root.right is None: return 1
        # left and right node
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)

    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # dfs iterative
        # stack
        # last in first out

        if root is None: return 0
        max_tracker = float('-inf')
        stack = [[root, 1]]
        while stack:
            current = stack.pop()
            cur_node, cur_depth = current
            if cur_node.left is None and cur_node.right is None: # a leaf
                max_tracker = max(max_tracker, cur_depth)

            # left and right node
            if cur_node.left is not None: stack.append([cur_node.left, cur_depth + 1])
            if cur_node.right is not None: stack.append([cur_node.right, cur_depth + 1])


        return max_tracker
