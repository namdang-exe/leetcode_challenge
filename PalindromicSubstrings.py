# More optimal solution
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            # odd substrings
            L, R = i, i
            while 0 <= L < n and 0 <= R < n:
                if s[L] != s[R]:
                    break
                else:
                    res += 1
                    L -= 1
                    R += 1
            # even substrings
            L, R = i, i+1
            while 0 <= L < n and 0 <= R < n:
                if s[L] != s[R]:
                    break
                else:
                    res += 1
                    L -= 1
                    R += 1
        return res
