# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # concept
        # for every node,
        # swap its left with its right
        # then recursively do that with its child
        #      2
        #    /   \ 
        #   1     3
        #  / \   / \
        # 7   9 4   8
        
        # Steps
        # swap the left and right of node 2 --- 1, 3
        # then go to 3
        # swap 4 and 8 - the left and right of node 3
        # then we go down => it's null => return itself
        # go to 1
        # swap 7 and 9 - the left and right of node 3
        
        return self.recursion(root)
        
    def recursion(self, root):
        # dfs recursive
        # base case
        if root is None: return root
        
        # recursion
        root.left, root.right = root.right, root.left        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
