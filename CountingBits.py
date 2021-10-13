# Dynamic Programming with Memoise, O(n) time
class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0 -  00 00 - 0
        # 1 -  00 01 - 1 + cache[n-1] | 1       ==> 1 is the OFFSET
        # 2 -  00 10 - 1 + cache[n-2] | 1
        # 3 -  00 11 - 1 + cache[n-2] | 2
        
        # 4 -  01 00 - 1 + cache[n-4]
        # 5 -  01 01 - 1 + cache[n-4]
        # 6 -  01 10 - 1 + cache[n-4]
        # 7 -  01 11 - 1 + cache[n-4]
        
        # 8 -  10 00 - 1 + cache[n-8]
         
        # => It reset every 4 unit
        # => It offsets whenevery it double (i.e. 1,2,4,8,...)
        # how to check for offset: multiple the current offset
        # e.g 2*2 == 3? 2*2 == 4?
        
        # code
        cache = [0] * (n+1)
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            cache[i] = 1 + cache[i - offset]
        return cache
