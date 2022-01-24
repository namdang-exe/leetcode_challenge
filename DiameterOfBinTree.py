# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_diam = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # dfs recursive
        # The furthest distance will be from two leaves
        # Algo:
        # find the sum of the furthest left path and right path
        # update the max tracker if that sum is greater than the current value of max tracker
        
        self.recursion(root)
        return self.max_diam
    def recursion(self, root):
        # base case
        if root is None: return 0
        
        # recursively find the longest path in
        # both left child and right child
        left = self.recursion(root.left)
        right = self.recursion(root.right)
        
        # update the max tracker if left_path plus right_path is larger
        self.max_diam = max(self.max_diam, left + right)
        
        # return the longest one between left_path and right_path;
        # remember to add 1 for the path connecting the node and its parent
        return max(left, right) + 1
