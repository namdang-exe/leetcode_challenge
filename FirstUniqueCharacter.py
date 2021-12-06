# Hashmap to count the freq of the letters
# loop through list to find first letter with freq == 1
# return 1 if not
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        # {l:1, e:2}
        s = list(s)
        for i in range(len(s)):
            if cnt[s[i]] == 1: 
                return i
            
        return -1
