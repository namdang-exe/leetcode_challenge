# DP tabulation
# O(n) time
# O(n) space
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        cur_sum = [0] * n
        max_sum = [0] * n
        cur_sum[0], max_sum[0] = nums[0], nums[0]
        for i in range(1, n):
            num = nums[i]
            cur_sum[i] = max(cur_sum[i-1] + num, num)
            max_sum[i] = max(max_sum[i-1], cur_sum[i])
        return max_sum[-1]
            
