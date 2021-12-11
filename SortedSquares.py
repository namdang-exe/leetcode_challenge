# O(n) time
# O(n) space
from collections import deque
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = deque()
        left, right = 0, len(nums) - 1 
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                squares = nums[right] ** 2
                right -= 1
            else:
                squares = nums[left] ** 2
                left += 1
            res.appendleft(squares)
        return res
