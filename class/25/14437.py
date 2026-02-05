def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}

    sr = 0
    if len(d) >= 2: sr = sum(d) // len(d)
    if sr % 1000 == 313:
        return sr
    return 0


c = 0

for num in range(1, 700_000)[::-1]:
    if x := f(num):
        c += 1
        print(num, x)
        if c == 7:
            break
