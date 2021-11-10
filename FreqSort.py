# Hashmap and Sort
# O(nlogn) Time , O(n) space

class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        # t: 1, r: 1, e: 2
        sorted_cnt = sorted(cnt.items(), key=lambda pairs:pairs[1], reverse=True)
        res = []
        for key, val in sorted_cnt:
            res += [key]*val
        return "".join(res)
