def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2
    i = 3
    while i * i < num +1:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2
    if num > 2:
        d += [num]
    five = []
    for k in d:
        if k%100 == 12:
            for b in d:
                if d.count(b) == 5:
                    five.append(b)
                    return d
    return []
cnt = 0
for i in range(5_000_000, 10**20):
        if fact(i):
            print(i, )