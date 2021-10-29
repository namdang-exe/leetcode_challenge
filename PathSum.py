# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # dfs iterative
        # stack
        # last in first out
        if not root:
            return False
        
        # [root, 5]
        stack = [[root, root.val]]
        while stack:
            current = stack.pop()
            cur_node, cur_sum = current
            # if it's a leaf, then compare w target
            if not cur_node.left and not cur_node.right:
                if cur_sum == targetSum:
                    return True
            
            # left and right node
            if cur_node.left: stack.append([cur_node.left, cur_sum + cur_node.left.val])
            if cur_node.right: stack.append([cur_node.right, cur_sum + cur_node.right.val])                
                
        return False
