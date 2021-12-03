# Brute force
class Solution:
    def numDecodings(self, s: str) -> int:
        s = list(s)
        n = len(s)
        return self._helper(s, 0, n)
    
    def _helper(self, s, i, n):
        """
        Recursive function
        s: list of digit
        i: index
        n: len of s
        """
        # base cases
        if i >= n: return 1
        if i < n and s[i] == "0": return 0
        if n - i == 1: return 1
        
        # recursion
        answer = self._helper(s, i+1, n) 
        if int(s[i] + s[i+1]) <= 26:
            answer += self._helper(s, i+2, n) 
            
        return answer
