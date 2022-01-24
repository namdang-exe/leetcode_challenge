# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # dfs recursive approach
        
        # if the node from one of the tree is null, 
        # assign the other non-null node to the resultant tree
        # at every node, compare the current value, 
        # the resultant tree's node's current value
        # = the sum of the val of 2 tree's current node
        # keep updating the left and right of the resultant tree by calling the function again
        return self.recursion(root1, root2)
        
        
    def recursion(self, root1, root2):
        # base case
        if root1 is None: return root2
        if root2 is None: return root1
        
        if root1 and root2:
            root1.val = root1.val + root2.val
        
        root1.left = self.recursion(root1.left, root2.left)
        root1.right = self.recursion(root1.right, root2.right)
            
        return root1
