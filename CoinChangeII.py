# Recursion with Memoize O(amount*n)


class Solution:
    def __init__(self):
        self.mem = {}
        
    def change(self, amount: int, coins: List[int]) -> int:
        coins = sorted(coins)
        n = len(coins)
        return self.recursion(amount, coins, n)
        
    def recursion(self, remain, coins, n):
        # [1,2,5], and amt = 5
        # Problem can be broken into 2 subproblems:
        #   1. Subproblem that contains all coins and
        #      subtract the last coin value from the remain
        #   E.g. 5-5 = 0, [1,2,5]
        #   2. Subproblem that does not contain the last coin, the remain stays the same
        #   E.g. 5,[1,2]
        
        # Memoize
        if self.mem.get((remain, n)) is not None:
            return self.mem[(remain,n)]
        # base cases
        if remain == 0:
            return 1
        if remain < 0 or n == 0:
            return 0
        res = self.recursion(remain - coins[n-1], coins, n) + self.recursion(remain, coins, n-1)
        self.mem[(remain, n)] = res
        return res
