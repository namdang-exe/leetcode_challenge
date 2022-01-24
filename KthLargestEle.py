# use min heap
# pop all min element 
# until we have k elements left in the array
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        # this ensures we only have k largest elements
        while len(self.nums) > k:
            heapq.heappop(self.nums)
        
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        # edge case 
        # when self.nums is None and k = 1
        # whatever we push is the largest number
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)    
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
