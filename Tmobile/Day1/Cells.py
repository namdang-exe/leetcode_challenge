def activeCells(nums, d):
    for j in range(d):
        out = []
        for i in range(8):
            if i - 1 < 0:
                L, R = 0, nums[i + 1]
            elif i + 1 == 8:
                L, R = nums[i - 1], 0
            else:
                L, R = nums[i - 1], nums[i + 1]
            # after we got the neighbor, compare them
            if L == R:  # both active or inactive
                out.append(0)
            else:
                out.append(1)
        nums = out

    return nums


nums = [1, 0, 0, 1, 0, 1, 0, 1]
print(activeCells(nums, 2))
