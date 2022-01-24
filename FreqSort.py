# Heap + hashmap
# O(nlogn)
from collections import Counter
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        # build hashmap for frequency
        cnt = Counter(s)
        
        # build heap
        heap = [(-v, k) for k,v in cnt.items()]
        # min heap
        heapq.heapify(heap)
        # (-2, e), (-1, r), (-1, t)
        res = []
        while heap:
            v, k = heapq.heappop(heap)
            res += [k] * -v
        return "".join(res)
