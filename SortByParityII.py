class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # One pass, 2 arrays
        odd = []
        even = []
        for num in nums:
            # even
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        out = []
        for e, o in zip(even, odd):
            out.append(e)
            out.append(o)
        return out
