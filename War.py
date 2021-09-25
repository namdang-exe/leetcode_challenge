def defuseBomb(nums, k):
    s = len(nums)
    out = []
    for i in range(s):
        if i + k > len(nums) - 1:
            nums += [nums[i+k-s]]
        sums = sum(nums[i + 1:i + k + 1])
        out.append(sums)
    return out


nums = [4, 2, -5, 11]
print(defuseBomb(nums, 3))
