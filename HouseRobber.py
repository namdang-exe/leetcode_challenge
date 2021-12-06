# Brute force recursion
# O(2^n) time
# O(1) space
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 2: return max(nums)
        
        def dfs(i):
            # dfs recursion
            # base case
            if i >= n: return 0
            if n - i == 1: return nums[i]
            
            res = max(nums[i] + dfs(i+2), nums[i+1] + dfs(i+3))
            return res
        
        return dfs(0)
