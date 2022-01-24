# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # dfs recursive approach
        # if p.val and q.val both less than root.val,
        # the LCA will be in one of nodes in the left subtree
        # elif p.val and q.val both greater than root.val,
        # the LCA will be in one of nodes in right subtree
        # else root.val == p or q: LCA is the root
        
        return self.recursion(root, p, q)
        
        
    def recursion(self, root, p, q):
        # base case:
        
        if p.val < root.val and q.val < root.val:
            return self.recursion(root.left, p, q)
        
        if p.val > root.val and q.val > root.val:
            return self.recursion(root.right, p, q)
        
        else:
            return root
