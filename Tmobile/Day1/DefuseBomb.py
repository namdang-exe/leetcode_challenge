# Not optimal
def defuseBomb(nums, s, k):
    out = []
    for i in range(len(nums)):
        if i + k >= len(nums):
            nums += [nums[i + k - s]]
        out.append(sum(nums[i + 1:i + k + 1]))
    return out


nums = [4, 2, -5, 11]
s = 4
k = 3
print(defuseBomb(nums, s, k))
