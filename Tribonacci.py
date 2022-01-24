# DP tabulation (table)
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1
        
        one, two, three = 0, 1, 1
        for i in range(n-2):
            temp = three
            three = one + two + three
            one, two = two, temp
            
        return three
