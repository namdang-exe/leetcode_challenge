# Linear DP
# Greedy?
# dp for max sum profit
# daily_profit variable for daily profit 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        daily_profit = 0
        dp = [0] * n
        
        for i in range(1, n):
            price = prices[i]
            daily_profit = price - prices[i-1]
            dp[i] = max(dp[i-1], dp[i-1] + daily_profit)
            
        return dp[-1]
