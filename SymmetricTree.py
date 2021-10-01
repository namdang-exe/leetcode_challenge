# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # base case
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)
        
    def isMirror(self, left, right):
        # base case
        if left is None and right is None: return True   
        if left is None or right is None: return False
        
        # if left and right are not none:
        if left.val == right.val:
            out_pair = self.isMirror(left.left, right.right)
            in_pair = self.isMirror(left.right, right.left)
            return out_pair and in_pair
        else: 
            return False
