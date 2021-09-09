nums = [0,4,3,0]
target = 0

needed_idx = []
hash_map = {}

# Subtracted from target
for i in range(len(nums)):
    diff = target - nums[i]
    if i == 0:
        hash_map[0] = nums[0]
    elif diff in hash_map.values():
        needed_idx.append(i)
        needed_idx.append(list(hash_map.keys())[list(hash_map.values()).index(diff)])
    else:
        hash_map[i] = nums[i]

print(needed_idx)

# O(n**2)
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == target:
#             needed_idx.append(i)
#             needed_idx.append(j)
#
# print(f"The answer is {needed_idx}")
