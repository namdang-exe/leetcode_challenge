# Dynamic Programming
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        min_price = prices[0]
        
        for i in range(1,len(prices)):
            dp[i] = max(dp[i-1], prices[i] - min_price)
            min_price = min(prices[i], min_price)
            
        return dp[-1]
