# DP with tabulation
# O(n) time 
# O(n) space

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices) + 1
        sold_dp = [0] * n
        hold_dp = [0] * n
        rest_dp = [0] * n
        sold_dp[0] = float("-inf")
        hold_dp[0] = float("-inf")
        for i in range(n-1):
            price = prices[i]
            sold_dp[i+1] = hold_dp[i] + price
            hold_dp[i+1] = max(hold_dp[i], rest_dp[i] - price) 
            rest_dp[i+1] = max(rest_dp[i], sold_dp[i])
            
        return max(sold_dp[-1], rest_dp[-1])
