# Dynamic Programming O(n) time
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # edge cases
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[1], dp[0])
        if n == 2:
            return dp[-1]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1], dp[i-2]+nums[i])
        return dp[-1]
