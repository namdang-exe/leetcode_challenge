# Brute force O(nlogn)
# sort nums
# loop thru nums
# return kth element

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]
        
