# Tabulation aka build a table
# Iterative
class Solution:
    def fib(self, n: int) -> int:
        # initialize table
        # [0,0,0,0,0,...]
        
        if n == 0:
            return 0
        if n== 1:
            return 1
        tab = [0] * (n+1)
        tab[1] = 1
        for i in range(2,n+1):
            tab[i] = tab[i-1] + tab[i-2]
        return tab[n]
