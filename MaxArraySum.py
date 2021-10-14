def maxSubsetSum(nums):
    n = len(nums)
    if n == 1 or n == 2:
        return 0
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[1], dp[0])
    # [3,-4,4,6,5] => [3,3]
    # [3,7,4,6,5] => [3,7]
    # what/if => we don't need to worry about it because we only need to find the max, and not keeping track of the indices
    for i in range(2, n):
        temp = dp[i - 2] + nums[i]
        dp[i] = max(nums[i], temp, dp[i - 1])
    return dp[-1]


nums = [3,5,-7,8,10]
print(maxSubsetSum(nums))
