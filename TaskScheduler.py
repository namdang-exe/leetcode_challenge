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
# heap + hashmap
# we want to pop the most frequent letter to the workload first
# A, A, A,B,C,D,E
# A, idle, idle, A, idle, idle, A
# A, B, C, A, D, E, A
# how to make sure it's not repeated?
# put what we popped in a temp []

from collections import Counter
from heapq import heappush, heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        max_heap = []
        for l, freq in cnt.items():
            heappush(max_heap, (-freq, l))
        res = 0
        while max_heap:
            i = 0 # index to track idle spots
            temp = [] # track letters just popped
            # this is "<=" instead of "<" because
            # we count the current spot for A
            # then n spot for idle
            while i <= n:
                res += 1
                # In case there's no repetitive task left to pop,
                # replace current spot with an "idle"
                # aka skip to next iteration (i++)
                # A,A,B,B example
                if max_heap:
                    freq, l = heappop(max_heap)
                    if freq != -1: # letter just popped can be reused if freq != -1
                        temp.append((freq+1, l))
                i += 1
                # after popped, if the max_heap is empty
                # that means no tasks left
                # we'll break only if
                # there's nothing in temp
                if not max_heap and not temp:
                    break
            for t in temp:
                heappush(max_heap, t)
        return res
