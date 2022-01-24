# DP tabulation
# Bottom up approach
# 2 pointers 
# O(n) time
# O(1) space
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        one, two = 0, 0
        for i in range(n):
            temp = two
            two = max(nums[i]+one, two)
            one = temp
        return two
