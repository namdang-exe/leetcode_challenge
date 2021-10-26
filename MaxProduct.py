# Brute force O(n^2) time
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_prod = nums[0]
        for i in range(n):
            cur_prod = nums[i]
            for j in range(i+1, n):
                cur_prod *= nums[j]
                max_prod = max(max_prod, cur_prod, nums[j])
        return max_prod
    
