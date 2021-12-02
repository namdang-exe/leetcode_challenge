# DP tabulation
# bottom up 
# O(n) time
# O(n) space
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices) + 1
        sold = [0] * n
        held = [0] * n
        rest = [0] * n        
        sold[0] = float('-inf')
        held[0] = float('-inf')
        
        for i in range(n-1):
            price = prices[i]
            sold[i + 1] = held[i] + price - fee
            held[i + 1] = max(held[i], sold[i] - price, rest[i] - price)
            rest[i + 1] = max(rest[i], sold[i])
            
        return max(sold[-1], rest[-1])
