# TODO: Optimized initialization
def defuseBomb(nums, s, k):
    out = []
    # Initialize sum
    cur_sum = sum(nums[1:k + 1])
    out.append(cur_sum)
    for i in range(1, s):
        cur_sum = cur_sum + nums[(i + k) % s] - nums[i]
        out.append(cur_sum)
    return out


nums = [4, 2, -5, 11]
s = 4
k = 3
print(defuseBomb(nums, s, k))
