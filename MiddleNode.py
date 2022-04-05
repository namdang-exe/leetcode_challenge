"""
Brute force
Store all node in an array
return mid pos of the array
Time: O(n)
Space: O(n)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge cases
        if head.next is None: return head
        res = []
        while head:
            res.append(head)
            head = head.next
        return res[len(res)//2]
