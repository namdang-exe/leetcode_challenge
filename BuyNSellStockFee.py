# Recursion
# O(2^n) time
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        def dfs(i, can_buy):
            # recursive function
            # base cases
            if i >= n: return 0
            
            # recursion
            price = prices[i]
            if can_buy:
                buy = dfs(i + 1, False) - price
                hold = dfs(i + 1, True)
                result = max(buy, hold)
            else:
                sell = dfs(i+1, True) + price - fee
                hold = dfs(i + 1, False)
                result = max(sell, hold)
                
            return result
        
        return dfs(0, True)
