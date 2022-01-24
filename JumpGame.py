# Greedy algorithm
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n -1
        for i in range(n-1)[::-1]:
            # Can I reach the goal from my current position?
            # if yes, move the goal post to current position 
            if nums[i] + i >= goal:
                goal = i
        return goal == 0
