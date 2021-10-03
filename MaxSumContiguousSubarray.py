# Max sum of any contiguous subarray of size k
def maxSumContiguousSubarray(nums, k):
    max_sum = float('-inf')
    cur_sum = 0
    start = 0
    for end, val in enumerate(nums):
        cur_sum += val
        if end - start + 1 == k:
            max_sum = max(max_sum, cur_sum)
            cur_sum -= nums[start]
            max_sum = max(max_sum, cur_sum)
            start += 1

    return max_sum


nums = [2, 3, 4, 1, 5]
print(maxSumContiguousSubarray(nums, 3))
