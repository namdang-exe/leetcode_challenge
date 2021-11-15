import heapq

# def max_heapify(nums, heapSize, i):
#     # recursive
#     l = 2 * i
#     r = 2 * i + 1

#     # compare left and right, but don't swap the value yet
#     # swap the Index
#     largest = i
#     if l < heapSize and nums[largest] < nums[l]:
#         largest = l
#     if r < heapSize and nums[largest] < nums[r]:
#         largest = r
#     if largest != i:
#         nums[largest], nums[i] = nums[i], nums[largest]
#         # recursively do this for the child node
#         max_heapify(nums, heapSize, largest)

def max_heapify(nums, n, i):
    # iterative

    done = False

    while not done:
        largest = i # root
        l = 2*i # left
        r = 2*i + 1 # right

        if l < n and nums[largest] < nums[l]:
            largest = l
        if r < n and nums[largest] < nums[r]:
            largest = r
        if largest != i:
            nums[largest], nums[i] = nums[i], nums[largest]
            i = largest
        else:
            done = True


# def min_heapify(nums, n, i):
#     # recursion
#     # same concept with max_heapify()
#     l = 2*i
#     r = 2*i + 1

#     smallest = i
#     if l < n and nums[smallest] > nums[l]:
#         smallest = i
#     if r < n and nums[smallest] > nums[r]:
#         smallest = r
#     if smallest != i:
#         nums[smallest], nums[i] = nums[i], nums[smallest]
#         min_heapify(nums, n, smallest)

def min_heapify(nums, n, i):
    # iterative
    done = False

    while not done:
        l = 2*i
        r = 2*i + 1
        smallest = i
        
        if l < n and nums[smallest] > nums[l]:
            smallest = l
        if l < n and nums[smallest] > nums[r]:
            smallest = r
        if smallest != i:
            nums[smallest], nums[i] = nums[i], nums[smallest]
            i = smallest
        else:
            done = True 



nums = [2,1,4,14,5,3]
n = len(nums)
max_heap = nums[:]
# build a max heap 
for i in range(n//2+1)[::-1]:
    max_heapify(max_heap, n, i)
print("Max heap is ", max_heap)
# build a min heapq
min_heap = nums[:]
for i in range(n//2 + 1)[::-1]:
    min_heapify(min_heap, n, i)
print("Min heap is ", min_heap)
res = nums[:]
heapq.heapify(res)
print("The result for min heap is: ", res)
res = [-n for n in nums]
heapq.heapify(res)
res = [-n for n in res]
print("The result for max heap is: ", res)
