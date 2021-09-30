from collections import Counter


def sortFreq(nums):
    # [1 2 2 3 3 3 4 4 5 5 5 5 6 6 6 7 8 9 10]
    cnt = Counter(nums)
    sorted_cnt = sorted(cnt.items(), key=lambda pair: pair[1], reverse=True)
    # return an array [(2,3), (3,4),...]
    out = []
    for key, val in sorted_cnt:
        temp = [key] * val
        # [2,2,2]
        out += temp
    return out


nums = [3, 2, 2, 2, 1, 4, 4, 5]
print(sortFreq(nums))
