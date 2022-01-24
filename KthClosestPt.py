# Second approach
# Instead of creating a heap of size k
# we use heappushpop instead
# O(nlogk)
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        # O(nlogk)
        for point in points:
            x, y = point
            dist = -(x**2+y**2)**0.5
            if len(heap) < k:
                # max heap
                # [(dist, x,y)]
                heapq.heappush(heap,(dist, x,y))
            else:
                heapq.heappushpop(heap, (dist, x, y))
        return [[x,y] for (dist, x,y) in heap]
