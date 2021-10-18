# Dynamic Programming O(n) time O(1) space
class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0
        for n in nums:
            new_rob = max(one + n, two)
            one = two
            two = new_rob
        return two
