class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Recursion
        
        # base case
        if n == 0: return False
        if n == 1: return True
        
        if n % 3 != 0: 
            return False
        else:
            return self.isPowerOfThree(n/3)
