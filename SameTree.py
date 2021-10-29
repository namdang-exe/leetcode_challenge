# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # bfs iterative
        # queue
        
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        qu = deque([[p,q], ])
        while qu:
            current = qu.pop()
            cur_p, cur_q = current                   

            if cur_p.val != cur_q.val:
                return False
            
            # left and right node:
            if not cur_p.left and cur_q.left:
                return False
            if not cur_p.right and cur_q.right:
                return False
            if cur_p.left and not cur_q.left:
                return False
            if cur_p.right and not cur_q.right:
                return False
            
            if cur_p.left and cur_q.left: 
                qu.appendleft([cur_p.left, cur_q.left])
            if cur_p.right and cur_q.right: 
                qu.appendleft([cur_p.right, cur_q.right])

        return True
