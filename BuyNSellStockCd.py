# DP  tabulation
# O(n) time 
# O(1) space

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold = float("-inf")
        held = float("-inf")
        rest = 0
        for price in prices:
            temp = sold
            sold = held + price
            held = max(held, rest - price)
            rest = max(rest, temp)
            
        return max(rest, sold)
