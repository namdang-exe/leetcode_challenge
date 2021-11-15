# max heap
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        def max_heapify(nums, n, i):
            l = 2*i
            r = 2*i + 1
            largest = i
            if l < n and nums[largest] < nums[l]:
                largest = l
            if r < n and nums[largest] < nums[r]:
                largest = r
            if largest != i:
                nums[largest], nums[i] = nums[i], nums[largest]
                max_heapify(nums, n, largest)
                
        if self.nums is None: 
            heap = []
        else:
            heap = [-num for num in self.nums]
        heap += [-val]
        n = len(heap)
        heapq.heapify(heap)
        res = 0
        for i in range(self.k):
            res = heapq.heappop(heap)
        self.nums += [val]
        return -res


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
