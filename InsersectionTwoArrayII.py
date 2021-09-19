from collections import Counter

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

res = []
cnt = Counter(nums1)
for num in nums2:
    if cnt[num] > 0:
        res.append(num)
        cnt[num] -= 1

print(res)