class Solution:
    def isUgly(self, n: int) -> bool:
        def max_divide(a,b):
            # we need to divide it to b number
            # b can be 2,3,5
            # until it cant be divided anymore
            while a % b == 0:
                # not rounded to a whole integer
                a /= b
            return a
        
        # edge cases
        if n == 0: return False
        if n == 1: return True

        n = max_divide(n, 2)
        n = max_divide(n, 3)
        n = max_divide(n, 5)
        
        return n == 1
