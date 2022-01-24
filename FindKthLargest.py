# Another heap sol
# O(k + nlogk) = > O(nlogk)
# we will use min heap

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min heap
        heap = nums[:k]
        heapq.heapify(heap) # O(k)
        
        for num in nums[k:]:
            # if the number is even smaller than the current one, ignore
            if num > heap[0]:         
                heapq.heapreplace(heap, num) # O(logk)
        return heap[0]
