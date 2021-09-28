from collections import Counter


def sortFreq(nums):
    cnt = Counter(nums)
    sorted_cnt = sorted(cnt.items(), key=lambda pair: pair[1], reverse=True)
    out = []
    for val, freq in sorted_cnt:
        out += [val] * freq
    return out


nums = [3, 2, 2, 2, 1, 4, 4, 5]
print(sortFreq(nums))
