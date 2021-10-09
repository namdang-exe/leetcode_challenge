# Sliding window + hashmap
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        # len
        M = len(s)
        N = len(p)

        cnt_p = Counter(p)
        cnt_w = Counter(s[:N - 1])
        start = 0
        for end in range(N - 1, M):
            # cb a - end : 2
            cnt_w[s[end]] = cnt_w.get(s[end], 0) + 1
            if cnt_w == cnt_p:
                res.append(start)
            cnt_w[s[start]] -= 1
            if cnt_w[s[start]] == 0:
                cnt_w.pop(s[start])
            start += 1
        return res


