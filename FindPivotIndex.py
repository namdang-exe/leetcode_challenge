class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if S - nums[i] - left_sum == left_sum:
                return i
            left_sum += nums[i]
        return -1
