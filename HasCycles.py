# if the node point to null => reach the end => return false
# use hashset to store the node object
# if node in hashset => it has a cycle => return true
# Time: O(n) - visit each node once
# Space: O(n) - store all node in the hashset

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head is not None:
            if head in seen: 
                return True
            else: 
                seen.add(head)
            head = head.next
        return False
