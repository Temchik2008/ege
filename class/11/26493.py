def g(n):
    if n >= 52000:
        return n/10 +30
    return g(n+1) - 1/2
def f(n):
    if n >=67:
        return n
    return 3*(g(n-2) -1)
print(f(10007))