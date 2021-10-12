# Recursive with Memoise
class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        def fibSeq(cache, n):
            if cache.get(n) is not None:
                return cache[n]
            if n == 0: return 0
            if n == 1: return 1
            else: 
                res = fibSeq(cache, n-1) + fibSeq(cache, n-2)
                cache[n] = res
                return res
        return fibSeq(cache, n)
