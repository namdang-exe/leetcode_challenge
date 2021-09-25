def neigh_cells(nums, day):
    today = nums
    for j in range(day):
        next_day = []
        for i in range(len(today)):
            if i - 1 < 0 and i + 1 == len(today):
                L, R = 0, 0
            elif i - 1 < 0:
                L, R = 0, today[i + 1]
            elif i + 1 == len(today):
                L, R = today[i - 1], 0
            else:
                L, R = today[i - 1], today[i + 1]
            if L == R:
                next_day.append(0)
            else:
                next_day.append(1)
        today = next_day
    return today


test = [1]
# 0[1,0,0,0,0,1,0,0]0
# [0 1 0 0 1 0 1 0]
print(neigh_cells(test, 1))
