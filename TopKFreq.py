# hashmap + heap
# O(klogn)
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        n = len(nums)
        # build a heap
        # max heap
        heap = [(-v, k) for k, v in cnt.items()]
        heapq.heapify(heap)
        res = []
        for i in range(k):
            needed = heapq.heappop(heap)
            res.append(needed[1])
            
        return res
