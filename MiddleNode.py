'''
Tortoise and Hare
slow and fast pointer
Fast ptr travel twice as fast as slow ptr
when fast reach the end, slow reach half
Time: O(n)
Space: O(1)
EAPF
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        try:
            slow = head
            fast = head.next
            while fast:
                slow = slow.next
                # travel twice as fast
                fast = fast.next.next
            return slow
        except:
            return slow
