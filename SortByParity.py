# 2 pointers, in-place 
# Time: O(n)
# Space: O(1)
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        # everything below i has a parity of 0
        # everything above j has a parity of 1
        while i < j:
            # (0,0) | (0,1) | (1,0) | (1,1)
            # 0,0 : i is correct, i++
            # 0,1 : both are correct, i++ j--
            # 1,0 : both are wrong, swap
            # 1,1 : j is correct, j--
            if nums[i] % 2 > nums[j] % 2:
                nums[i], nums[j] = nums[j], nums[i]
            if nums[i] % 2 == 0: i += 1
            if nums[j] % 2 != 0: j -= 1
        return nums
