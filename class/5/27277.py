def tri(x):
    res = ''
    while x != 0:
        res += str(x % 3)
        x //= 3
    return res[::-1] if res else '0'

for n in range(1, 1000):
    r = tri(n)
    if n % 3 != 0:
        r = '1' + r + r[-3:]
    else:
        r = r + tri(int(sum([int(i) for i in r]))
                    *8)
    r = int(r, 3)
    if 2250 > r > 1150:
        print(r)
