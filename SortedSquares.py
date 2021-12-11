# O(nlogn) time
# O(n) space
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            num = num**2
        return sorted(res) # O(nlogn)
