class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            # [3,2], [2,3] perms
            for perm in perms:
                perm.append(n)
            result += perms
            nums.append(n)
        return result
