# Dynamic Programming O(amount*n) time and O(amount) space

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount + 1)
        dp[0] = 0
        # [2], amt = 3
        for i in range(1, amount + 1):
            for c in coins:
                # if i == c, diff = 0 and dp[0] = 0 
                diff = i - c
                if diff >= 0:
                    dp[i] = min(dp[i], 1 + dp[diff])
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]
