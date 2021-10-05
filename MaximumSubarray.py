# Brute force O(n*3) sol
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarr = float('-inf')
        for i in range(len(nums)):
            # nums[0:0] = [] --- nums[0:1] = [-2]
            for j in range(i,len(nums)):
                max_subarr = max(max_subarr, sum(nums[i:j+1]))
        return max_subarr
                
