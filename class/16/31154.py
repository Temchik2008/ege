from functools import lru_cache

@lru_cache(None)

def f(n):
    if n == 1:
        return 1
    else:
        return (n-1 )* f(n-1)

for i in range(1, 200026):
    f(i)

print((f(17258) +3 *f(17257))/f(17256))