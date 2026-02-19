cnt = 0
for n in range(1000, 10000):
    n = str(n)
    if len(list(n)) == len(set(n)):
        d = [int(c) for c in n]
        if all(d[i] % 2 != d[i + 1] % 2 for i in range(3)):
            cnt += 1

print(cnt)