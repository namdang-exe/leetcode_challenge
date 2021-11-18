class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(1, len(nums)+1):
            if not i in set(nums):
                res.append(i)
                
        return res
