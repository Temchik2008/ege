from fnmatch import fnmatch

def f(num):
    d = set()
    d |= {1, num}
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num//i}
    return [len(d), sum(d)]

for n in range(22, 10**7):
    n = str(n)
    if fnmatch(n, '*2?2*') and n == n[::-1] and int(n)%53 == 0 and f(int(n))[0] > 30:
        print(n, f(int(n))[1])