from collections import Counter


def sortFreq(nums):
    cnt = Counter(nums)
    sorted_cnt = sorted(cnt.items(), key=lambda pair: pair[1], reverse=True)
    out = []
    for val, freq in sorted_cnt:
        out += [val] * freq
    return out


nums = [1, 2, 4, 5, 1]
print(sortFreq(nums, 5))
