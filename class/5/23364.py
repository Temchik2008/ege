ans =[]
def tri(x):
    res = ''
    while x != 0:
        res += str(x % 3)
        x //= 3
    return res[::-1] if res else '0'
for n in range(1, 1000):
    r = tri(n)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += tri((n%3)*5)
    if int(r, 3) > 150:
        ans.append(int(r, 3))
print(min(ans))