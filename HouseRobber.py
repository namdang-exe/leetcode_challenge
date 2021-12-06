# Recursion with Memoization
# O(n) time
# O(n) space
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}
        # {3:7}
        def dfs(i):
            # dfs recursion
            if i in cache: return cache[i]
            # base case
            if i >= n: return 0
            if n - i == 1: return nums[i]
            
            res = max(nums[i] + dfs(i+2), nums[i+1] + dfs(i+3))
            cache[i] = res
            return cache[i]
        
