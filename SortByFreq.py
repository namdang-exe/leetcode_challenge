from collections import Counter


def sortFreq(s, nums):
    cnt = Counter(nums)
    # auto sort by asc order
    sorted_cnt = sorted(cnt.items(), key=lambda pair: pair[1], reverse=True)
    # [(2, 3), (4, 2), (3, 1), (5, 1), (1, 1)]
    out = []
    for val, freq in sorted_cnt:
        out += [val] * freq
        # [2] * 3 = [2,2,2] + [] = [2,2,2] - output
    return out


# nums = [3, 2, 2, 2, 5, 4, 4, 1]
nums = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 8, 9, 10]
print(sortFreq(19, nums))
