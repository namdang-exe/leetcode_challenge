from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = max_sum = nums[0]
        start = 0
        for i in range(1, len(nums)):
            cur_sum = cur_sum + nums[i]
            if cur_sum < cur_sum - nums[start]:
                cur_sum = cur_sum - nums[start]
                start += 1
            else:
                if nums[i] > cur_sum:
                    cur_sum = nums[i]
                    start = i
            max_sum = max(max_sum, cur_sum)
        return max_sum
