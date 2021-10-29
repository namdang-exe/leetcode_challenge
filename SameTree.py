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
        
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        
        p_q = deque([p])
        q_q = deque([q]) 
        while p_q or q_q:
            cur_p = p_q.pop()
            cur_q = q_q.pop()
            if cur_p.val != cur_q.val:
                return False
            
            # left and right node:
            if cur_p.left is None and cur_q.left is not None:
                return False
            if cur_p.right is None and cur_q.right is not None:
                return False
            if cur_p.left is not None and cur_q.left is None:
                return False
            if cur_p.right is not None and cur_q.right is None:
                return False
            
            if cur_p.left is not None: 
                p_q.appendleft(cur_p.left)
            if cur_p.right is not None: 
                p_q.appendleft(cur_p.right)
            if cur_q.left is not None: 
                q_q.appendleft(cur_q.left)
            if cur_q.right is not None: 
                q_q.appendleft(cur_q.right)
        
        if len(p_q) != 0 or len(q_q) != 0:
            return False
        
        return True
