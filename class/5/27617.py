s = []
for n in range(1,10000):
    r = f'{n:b}'
    if n % 3 == 0:
        r = r + r[-3:]
    else:
        r = r + f'{(n%3 * 3):b}'
    if int(r, 2) < 150:
        s.append([n, int(r, 2)])
print(sorted(s))