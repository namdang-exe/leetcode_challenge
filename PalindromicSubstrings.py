# Brute force
class Solution:
    def countSubstrings(self, s: str) -> int:
        def check_pal(s):
            "This func will check if a string is a palindrome"
            if len(s) <= 1: return True
            left, right = 0, len(s) -1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i, n):
                if check_pal(s[i:j+1]):
                    res += 1
                    
