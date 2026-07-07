from string import printable

def six(x):
    res = ''
    while x != 0:
        res += str(x % 6)
        x //= 6
    return (res[::-1]) if res else '0'

cnt = []
n = 6**2030 +6**100
for x in range(1, 2031):
    res = six(n - x)
    cnt.append(res.count('0'))

print(max(cnt))