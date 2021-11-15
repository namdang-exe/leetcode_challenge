# Second approach
# Create a heap of size k
# O(nlogk)
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def eucli_dist(x,y):
            return (x**2+y**2)**0.5
        
        # [(dist, [x,y])]
        heap = [(-eucli_dist(x,y), [x,y]) for x,y in points[:k]]
        # build a max heap
        # O(k)
        heapq.heapify(heap)

        # add points to the heap
        # O(nlogk)
        for point in points[k:]:
            x, y = point
            if eucli_dist(x,y) < -heap[0][0]:
                heapq.heapreplace(heap, (-eucli_dist(x,y), [x,y]))
        # return the result array
        # O(k)
        res = []
        for val in heap:
            pt = val[1]
            res.append(pt)
        
        return res
