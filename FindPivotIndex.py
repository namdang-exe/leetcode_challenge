from itertools import accumulate

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        cum_left = list(accumulate(nums))
        cum_right = list(accumulate(nums[::-1]))[::-1]
        for i in range(n):
            # left = i - 1
            # right = i + 1
            left = cum_left[i-1] if i - 1 >= 0 else 0
            right = cum_right[i+1] if i+1 < n else 0
            if left == right:
                return i
        return -1
