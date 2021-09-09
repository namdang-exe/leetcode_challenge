nums = [3, 2, 4]
target = 6

sum = 0
needed_idx = []

# O(n(k-1))
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            needed_idx.append(i)
            needed_idx.append(j)

print(needed_idx)
