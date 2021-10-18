# House Robber II dynamic programming O(n) time O(n) space
# Reuse House Robber I sol but for 2 different nums list
# E.g. [1,2,1,1] =>  [2,1,1] and [1,2,1
# Do not include the first house for the first list
# Do not include the last house for the second list
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dp(nums):
            n = len(nums)
            if n == 1:
                return nums[0]
            if n == 2:
                return max(nums[0], nums[1])
            cache = [0] * n
            cache[0] = nums[0]
            cache[1] = max(nums[1], cache[0])
            for i in range(1, n):
                cache[i] = max(nums[i], cache[i-1], cache[i-2] + nums[i])
            return cache[-1]
        return max(dp(nums[:-1]), dp(nums[1:]))
