# Recursion
class Solution:
    def __init__(self):
        # {3: false} -- this a dead end
        self.cache = {}
        
    def canJump(self, nums: List[int]) -> bool:
        d = len(nums) - 1
        return self.helper(nums, 0, d)
    
    def helper(self, nums, i, d):
        """
        nums: list of jump length
        i: current pos
        d: destination
        """
        
        # Check cache
        if i in self.cache: return False
        
        # Base case 
        if i >= d: return True
        if nums[i] == 0: return False
        
        # Recursion
        jump_len = nums[i]
        for l in range(1, jump_len+1)[::-1]:
            idx = i + l
            res = self.helper(nums, idx, d)
            if res:
                return True
            else:
                self.cache[idx] = res
        return False
            
