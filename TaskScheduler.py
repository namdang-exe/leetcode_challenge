from collections import Counter
from heapq import heappop, heappush


def leastInterval(tasks, n):
    res, max_heap = 0, []
    for k, v in Counter(tasks).items():
        heappush(max_heap, (-1 * v, k))
    while max_heap:
        i, temp = 0, []
        while i <= n:
            res += 1
            if max_heap:
                x, y = heappop(max_heap)
                if x != -1:
                    temp.append((x + 1, y))
            if not max_heap and not temp:
                break
            else:
                i += 1
        for item in temp:
            heappush(max_heap, item)
    return res


tasks = ["A", "A", "A", "B", "C", "D", "E"]
n = 2
print(leastInterval(tasks, n))
