"""

# Recursive Approach O(amount**coin) time with memoize
# have n as a parameter
# take the last coin

# Memoize
# store (n, remain)



# if there is no coin permutation that can make remain, return -1
# E.g. [2], remain = 1 ====> return -1

# base cases
# remain == 0 => good path, + 1 to minCoins for every step to get here
# remain > 0 and n == 0 (aka ran out of coins) => bad path => mark this path a big num
# so that the minCoins tracker will ignore this path
# remain < 0
# in other words, when subtract the coin value from remain and you get a negative value (or coins[n-1] > remain  **n = len(coins)), skip to the next coin in the list



# [1,2,5], amt = 11
# Problem can be divided into 2 subproblems:
#   1. Subproblem that contains all coins, remain - the last coin
#       Every time the subproblem call, + 1 to minCoins    
#       E.g. 11 - 5 = 6, [1,2,5] => 6 will have all coins to work with
#
#   2. Subproblem that does not contain the last coin, remain stay the same
#       E.g. 11, [1,2]


"""
class Solution:
    def __init__(self):
        self.mem = {}
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        coins = sorted(coins)
        minCoins = self.minCoinsRecursion(coins, amount, n)
        if minCoins == float('inf'):
            return -1
        return minCoins
    
        
    def minCoinsRecursion(self, coins, remain, n):
        if self.mem.get((n, remain)) is not None:
            return self.mem[(n, remain)]
        if remain == 0:
            return 0
        if remain > 0 and n == 0:
            return float('inf')
        if coins[n-1] > remain:
            return self.minCoinsRecursion(coins, remain, n-1)
        minCoins = min(1 + self.minCoinsRecursion(coins, remain-coins[n-1], n), self.minCoinsRecursion(coins, remain, n-1))
        self.mem[(n,remain)] = minCoins
        return minCoins
