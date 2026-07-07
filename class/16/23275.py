from functools import lru_cache

@lru_cache(None)

def g(n):
    if n <10:
        return 2 *n
    else:
        return g(n-2)
@lru_cache(None)

def f(n):
    return 2 * (g(n -3)+8)
print(f(1548))