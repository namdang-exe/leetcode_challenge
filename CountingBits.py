# Brute Force O(n^2)

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            binary = bin(i)
            cnt = Counter(binary)
            res.append(cnt['1'])
        return res
