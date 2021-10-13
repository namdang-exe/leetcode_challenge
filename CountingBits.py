# Brute Force O(nlgn), pure Math approach

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            # use pure math
            cnt = 0
            while i != 0:
                if i % 2 == 1:
                    cnt += 1
                i //= 2
            res.append(cnt)
        return res
