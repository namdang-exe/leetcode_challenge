# bottom up approach
cache = {}
def fib(cache,n):
    for k in range(n+1):
        if k < 2:
            res = 1
        else: 
            res = cache[k-1] + cache[k-2]
        cache[k] = res
    return cache[n]

print(fib(cache, 7))
