# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # recursive
        
        # base case
        # if they both empty => Same
        if not p and not q:
            return True
        # if one of them is empty => Not the same
        if not p or not q:
            return False
        # if p.val == q.val => Check left and right
        if p.val == q.val:
            if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True
            else:
                return False
            
        # if their val is not equal => Not the same
        return False
