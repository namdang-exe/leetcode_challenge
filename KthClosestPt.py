# First approach - min heap
# O(klogn)
#[(dist, [x,y])]
# pop the heap k time
# then return the value of the last pop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def eucli_dist(x,y):
            return (x**2 + y**2)**0.5
        heap = [(eucli_dist(x,y), [x,y]) for x,y in points]
        # min heap
        # O(n)
        heapq.heapify(heap)
        res = []
        # pop kth closest point
        # O(klogn)
        for i in range(k):
            val = heapq.heappop(heap)
            pt = val[1]
            res.append(pt)
        return res
