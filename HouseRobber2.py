# House Robber II dynamic programming O(n) time O(1) 
# Reuse House Robber I sol but for 2 different nums list
# E.g. [1,2,1,1] =>  [2,1,1] and [1,2,1
# Do not include the first house for the first list
# Do not include the last house for the second list
class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.dp(nums[1:]), self.dp(nums[:-1]))
    
    def dp(self, nums):
        # return 0 if [] passed as an argument
        one, two = 0, 0
        for n in nums:
            new_rob = max(one + n, two)
            one = two
            two = new_rob
        return two
