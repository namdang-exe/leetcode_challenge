nums = []


def summary_ranges(nums):
    output = [[]]
    index = 0
    # Be careful empty list
    if not nums:
        return nums
    output[0] += [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            output[index] += [nums[i]]
        else:
            index += 1
            output.append([nums[i]])

    for i in range(len(output)):
        if len(output[i]) >= 2:
            output[i] = (f"{min(output[i])}->{max(output[i])}")
        else:
            output[i] = (str(output[i][-1]))

    return output


print(summary_ranges(nums))
