# A little more efficient O(n^2) sol
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                max_sum = max(max_sum, cur_sum)
        return max_sum
                
