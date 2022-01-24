# Start in the middle and branching out method

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 0
        res = None
        for i in range(n):
            l, r = i, i
            # odd substring
            while l >= 0 and r < n and s[l] == s[r]:
                if max_len < r - l + 1 :
                    max_len = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
            # even substring
            l,r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if max_len < r - l + 1 :
                    max_len = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
        return res
                
