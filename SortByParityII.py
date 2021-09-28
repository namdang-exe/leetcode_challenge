class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # This method works because numbers of even number = numbers of odd number
        # Time: O(n)
        # Space: O(1)
        # 2 pointers method
        # if pointer points to the correct value, move to the next index (pointer++)
        # if both pointers point to wrong values, swap their value
        # Idea behind: Eventually both pointers will point to the wrong value if the list is not already sorted
        # it is because numbers of even number = numbers of odd number
        evenPt = 0
        oddPt = 1
        while evenPt < len(nums) and oddPt <len(nums):
            if nums[evenPt] % 2 == 0:
                evenPt += 2
            elif nums[oddPt] % 2 != 0:
                oddPt += 2
            # when both pointers point to a wrong value
            else:
                nums[evenPt], nums[oddPt] = nums[oddPt], nums[evenPt]
        return nums
