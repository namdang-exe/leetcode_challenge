class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map = {
            'I': 1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D':500, 'M':1000
        }
        total = 0
        i = 0
        s = list(s)
        while i < len(s):
            # Subtract the next num by the current num 
            if i + 1 < len(s) and hash_map[s[i]] < hash_map[s[i+1]]:
                total = total + hash_map[s[i+1]] - hash_map[s[i]]
                i += 2
            # Add current val to total
            else:
                total += hash_map[s[i]]
                i += 1
        return total
