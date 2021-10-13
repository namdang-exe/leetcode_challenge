# Recursive Approach O(2^n)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def recursion(nums, index, cur):
            # base case
            if index == len(nums):
                return 1 if cur == 0 else 0
            # first case - plus sign
            # second case - negative sign
            return recursion(nums, index + 1, cur + nums[index]) + recursion(nums, index + 1, cur - nums[index])
        return recursion(nums, 0, target)
