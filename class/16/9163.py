from functools import lru_cache

@lru_cache(None)

def f(n):
    if n >= 2025: return n
    return f(n +1) - f(n+2) +7

for i in range(1, 2025)[::-1]:
    f(i)

print(f'{2028:b}')