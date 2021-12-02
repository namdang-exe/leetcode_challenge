# Recursion with memoise

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # can_buy:
        # True: can buy 
        # False: sell
        # buy => i = i + 1
        # sell => i = i + 2
        cache = {} # (i, can_buy)
        
        def dfs(i, can_buy):
            # base cases
            if (i, can_buy) in cache: return cache[(i, can_buy)]
            if i >= n: return 0
            
            # recursion
            if can_buy:
                buy = dfs(i+1, False) - prices[i]
                cooldown = dfs(i+1, can_buy)
                res = max(buy, cooldown)
                cache[(i, can_buy)] = res
            else:
                sell = dfs(i + 2, True) + prices[i]
                cooldown = dfs(i + 1, can_buy)
                res = max(sell, cooldown)
                cache[(i, can_buy)] = res
                
            return cache[(i, can_buy)]
        
        n = len(prices)
        return dfs(0, True)
                
