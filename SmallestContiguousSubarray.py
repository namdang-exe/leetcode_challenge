# This algorithm will return the size of the smallest contiguous subarray with the sum >= target sum
# using sliding window
def sizeSmallestConSubarray(nums, target_sum):
    min_size = float('inf')
    cur_sum = 0
    start = 0
    for end, val in enumerate(nums):
        cur_sum += val
        while cur_sum >= target_sum:
            cur_sum_s = end - start + 1
            min_size = min(min_size, cur_sum_s)
            cur_sum -= nums[start]
            start += 1
    return min_size

nums = [2,4,2,5,1]
target_sum = 7
print(sizeSmallestConSubarray(nums, target_sum))
