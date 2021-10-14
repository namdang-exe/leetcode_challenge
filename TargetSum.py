# Recursive with Memoize
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        me = {}
        def dp(nums, me, index, cur_num):
            if me.get((index, cur_num)) is not None:
                return me[(index, cur_num)]
            if index == n: 
                return 1 if cur_num == 0 else 0
            # positive sign
            # negative sign
            
            res = dp(nums,me, index+1, cur_num+ nums[index]) + dp(nums,me, index+1, cur_num - nums[index])
            me[(index, cur_num)] = res
            return res
            
        return dp(nums, me, 0, target)
