# Recursion with Memoize
# O(n) time
# O(n) space
# Top down approach
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        cache = {}
        # {(0, True): 1, (1, False): 2}
        def dfs(i, can_buy):
            "Recursive function"
            # check cache
            if (i, can_buy) in cache: return cache[(i,can_buy)]
            
            # base cases
            if i >= n: return 0
            
            # recursion
            price = prices[i]
            if can_buy:
                buy = dfs(i + 1, False) - price
                hold = dfs(i + 1, True)
                result = max(buy, hold)
                cache[(i, can_buy)] = result
            else:
                sell = dfs(i+1, True) + price - fee
                hold = dfs(i + 1, False)
                result = max(sell, hold)
                cache[(i, can_buy)] = result
                
            return cache[(i, can_buy)]
        
        return dfs(0, True)
