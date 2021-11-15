# hashmap + heap
# O(n + 2k + nlogk) => O(nlogk)
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n)
        cnt = Counter(nums)
        n = len(nums)
        # build a heap
        # min heap
        heap = [(v,k) for k,v in list(cnt.items())[:k]]
        # O(k)
        heapq.heapify(heap)
        # add nums freq to heap
        # O(nlogk)
        for k, v in list(cnt.items())[k:]:
            if v > heap[0][0]:
                heapq.heapreplace(heap, (v,k))
        res = []
        # O(k)
        for i in range(len(heap))[::-1]:
            res.append(heap[i][1])
        return res
