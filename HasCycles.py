# Floyd's tortoise and hare
# 1 fast and slow pointer
# eventually the fast ptr will catch up w the slow ptr
# Time: O(n) why?
# it will catch up in a cycle
# - the total len is int
# - distance between fast and slow is int
# Space: O(1)
# EAFP

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            slow, fast = head, head.next
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
