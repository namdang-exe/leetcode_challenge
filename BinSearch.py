class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # recursive
        left, right = 0, len(nums) - 1
        return self.recursion(nums, left, right, target)
    def recursion(self, nums, left, right, target):
        # base case
        if left > right: return -1
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        
        if nums[mid] < target:
            # ignore the first half
            return self.recursion(nums, mid +1, right, target)
        if nums[mid] > target:
            # ignore the second half
            return self.recursion(nums, left, mid -1, target)
