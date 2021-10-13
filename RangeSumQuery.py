class NumArray:

    def __init__(self, nums: List[int]):
        self.cum = [0] + list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.cum[right+1] - self.cum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# Dynamic Programming

# [-2, 0, 3, -5, 2, -1]
#   0,-2,-2,1, -4, -2, -3

# if we want the sum range of [2:5] or [3,-5,2]
# we can calculate by using the sum of 
# [0:5] - [0:2] or sum([-2,0,3,-5,2]) - sum([-2,0,3])
