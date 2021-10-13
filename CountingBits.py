# Brute Force O(nlogn), Math approach

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            # use math
            cnt = 0
            # this take O(logn) because we can only divide an integer logn times
            while i != 0:
                if i % 2 == 1:
                    cnt += 1
                i //= 2
            res.append(cnt)
        return res
