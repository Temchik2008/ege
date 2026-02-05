def f(num):
    l = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            l |= {i, num // i}
    if len(l) >= 7:
        return [sorted(list(l))[::-1][6], len(l)]
    return 0

c = 0
for num in range(400_000_001, 100000000000000):
    if x := f(num):
        c += 1
        print(*x)
        if c == 5:
            break