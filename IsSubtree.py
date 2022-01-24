# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # dfs recursive solution
        
        # Check all nodes to see if any == subRoot
        # Code logic: if one of the case is True, return True for the whole thing (or operator)
        #           3
        #         /   \
        #        4     5
        #       / \     
        #      1   2
        
        # Ideas:
        # Check if 1 sub tree == subRoot : False => if 2 == subRoot: F => if 4 == subRoot: True
        # => return True
        
        # Algo:
        # If the current node == subroot's cur node,
        # compare the left node with subroot's left node,
        # the right node with subroot's right node
        # => they have to be equal to return True
        
        # sameTree() will compare subtree with subroot
        # => our main() will RECURSIVELY pass in different subtree as a parameter
        
        # recursion
        # base case
        # if root is null and subroot is not: is not subtree
        # if root is not null and subroot is null: is subtree
        # if root is null and subroot is null: pass to sameTree()
        # if root is not null and subroot is not null: pass to sameTree()
        if root is None and subRoot is not None: return False
        if root is not None and subRoot is None: return True
        
        if self.sameTree(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
        
    def sameTree(self, root, subRoot):
        # recursion function to check if subTree match subRoot
        # base case
        # if they both null => Same tree
        if root is None and subRoot is None: return True
        
        # if one of them is null => Not the same
        if root is None or subRoot is None: return False
        # if (root is None and subRoot is not None) or (root is not None and subRoot is None): return False
        
        # recursion
        if root.val == subRoot.val: 
            if self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right):
                return True
            else:
                return False
            
        # if root.val != subRoot.val: return False
        return False
        
