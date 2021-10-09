# Sliding window + hashmap
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # len
        M = len(s1)
        N = len(s2)

        cnt_s1 = Counter(s1)
        cnt_w = Counter(s2[:M - 1])
        start = 0
        for end in range(M - 1, N):
            # M -1 = 1
            # eid
            cnt_w[s2[end]] = cnt_w.get(s2[end], 0) + 1
            if cnt_w == cnt_s1:
                return True
            cnt_w[s2[start]] -= 1
            if cnt_w[s2[start]] == 0:
                cnt_w.pop(s2[start])
            start += 1
        return False


s1 = "ab"
s2 = "eidboaoo"
print(Solution.checkInclusion(s1, s2))
