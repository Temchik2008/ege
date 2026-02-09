def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2
    i = 3
    while i <= int(num ** 0.5):
        while num % i == 0:
            d += [i]
            num //= i
        i += 2
    if num > 1:
        d += [num]
    for i in d:
        if '5' not in str(i):
            return 0
    if len(d) == 5:
        return d
    return 0

cnt = 0
i = 13_475_125

while cnt < 5:
    r = fact(i)
    if r:
        print(i, max(r))
        cnt += 1
    i += 1
