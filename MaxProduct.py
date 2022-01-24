class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        cur_min = cur_max = 1
        for num in nums:
            temp = cur_max
            cur_max = max(num * cur_max, num * cur_min, num)
            cur_min = min(num * temp, num * cur_min, num)
            res = max(res, cur_max, cur_min)
        
        return res
