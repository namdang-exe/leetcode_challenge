# Tabulation without a table
# O(n) time
# O(1) space
class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        
        one, two = 0, 1
        for i in range(n-1):
            temp = two 
            two = one + two 
            one = temp 
        
        return two
