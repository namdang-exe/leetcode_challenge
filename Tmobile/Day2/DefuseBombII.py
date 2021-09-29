# Sliding window, defuse bomb optimized O(n)
def defuseBomb(nums, s, k):
    out = []
    if len(nums) == 0:
        return 0
    # Initialize sliding window sum
    sum_subarr = sum(nums[1:k + 1])
    out.append(sum_subarr)
    for i in range(1, s):
        idx = (i + k) % s
        sum_subarr = sum_subarr + nums[idx] - nums[i]
        out.append(sum_subarr)
    return out


nums = [4, 2, -5, 11, 6]
print(defuseBomb(nums, 5, 3))
