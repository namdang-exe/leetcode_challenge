# Brute force
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check_palindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        
        n = len(s)
        max_len = 0
        res = None
        for i in range(n):
            for j in range(i, n):
                if check_palindrome(s[i:j+1]):
                    if max_len < len(s[i:j+1]):
                        max_len = len(s[i:j+1])
                        res = s[i:j+1]
                        
        return res
