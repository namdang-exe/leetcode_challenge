# DP tabulation
# bottom up 
# 3 pointers
# O(n) time
# O(1) space
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sold = float('-inf')
        held = float('-inf')
        rest = 0
        
        for price in prices:
            temp_sold = sold
            sold = held + price - fee
            held = max(held, temp_sold - price, rest - price)
            rest = max(rest, temp_sold)
            
        return max(sold, rest)
