# Heap solution
# build a max heap O(n)
# extract kth largest
#   - loop through k
#   - swap the root with last node
#   - cut the size of the heap (to remove the last node)
#   - heapify the heap again
# Time: O(n + klogn)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def max_heapify(nums, n, i):
            left = 2 * i
            right = 2 * i + 1
            
            # compare current node with left and right
            # but we swap the index first, not the actual value
            largest = i
            if left < n and nums[largest] < nums[left]:
                largest = left
            if right < n and nums[largest] < nums[right]:
                largest = right
            
            if largest != i:
                # we swap the actual value
                nums[largest], nums[i] = nums[i], nums[largest]
                # when we swap the value, the tree below might not be a max heap anymore
                # so we apply recursively to the children nodes
                max_heapify(nums, n, largest)
                
        n = len(nums)
        # build a heap O(n)
        for i in range(n//2+1)[::-1]:
            max_heapify(nums, n, i)
            
        # extract kth largest
        # O(klogn)
        for i in range(k):
            nums[0], nums[n-1-i] = nums[n-1-i], nums[0]
            
            max_heapify(nums, n-1-i, 0)
            
        return nums[-k]
