# Recursion O(amount**n) time TLE


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins = sorted(coins)
        return self.recursion(amount, coins)
        
    def recursion(self, remain, coins):
        # [1,2,5], and amt = 5
        # Problem can be broken into 2 subproblems:
        #   1. Subproblem that contains all coins and
        #      subtract the last coin value from the remain
        #   E.g. 5-5 = 0, [1,2,5]
        #   2. Subproblem that does not contain the last coin, the remain stays the same
        #   E.g. 5,[1,2]
        
        # base cases
        if remain == 0:
            return 1
        if remain < 0 or len(coins) == 0:
            return 0
        
        return self.recursion(remain - coins[-1], coins) + self.recursion(remain, coins[:-1])
    
