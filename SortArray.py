class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Heap sort
        
        n = len(nums)
        def max_heapify(nums, n, i):
            l = 2 * i
            r = 2 * i + 1

            largest = i
            # compare with the left node, keep track of the largest index
            if l < n and nums[largest] < nums[l]:
                largest = l
            # compare w the right node:
            if r < n and nums[largest] < nums[r]:
                largest = r
            # because we know the left(i) and right(i) are max heap, this will be the base case
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                # there is a chance the children of the current node is not max heaps
                # so we call max_heapify on the children recursively
                max_heapify(nums, n, largest)
        
        # build a max heap
        for i in range(n//2+1)[::-1]:
            max_heapify(nums, n, i)
            
        # sort nums
        # because we have a max heap (not min), we will loop thru array reversely
        for i in range(n)[::-1]:
            nums[i], nums[0] = nums[0], nums[i]
            max_heapify(nums, i, 0)
        return nums
        # Time: O(nlogn)
        
