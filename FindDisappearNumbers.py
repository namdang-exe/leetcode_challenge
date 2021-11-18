class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        nums = set(nums)
        for i in range(1, n +1):
            if not i in nums:
                res.append(i)
                
        return res
