# x2 Kadane algorithm
# max Subarray circular = totalSum - min sum
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max = cur_min = 0
        max_sum = float('-inf')
        min_sum = float('inf')
        total = 0
        for num in nums:
            cur_max = max(cur_max + num, num)
            max_sum = max(max_sum, cur_max)
            cur_min = min(cur_min + num, num)
            min_sum = min(cur_min, min_sum)
            total += num
            
        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum
