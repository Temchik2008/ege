def f(num, sys):
    cnt = ''
    while num:
        cnt += str(num %sys)
        num //= sys

    return cnt[::-1]
cnt = []
for n in range(1, 1000):
    r = f(n, 4)
    b = str(n)[:-2]
    if  n % 4:
        r = r + str(f(b, 4))
    else:
        c = (n %4) * 4
        c = f(c, 4)
        r = r + c
    if int(r, 4) > 291:
        cnt.append(int(r,4))
print(min(cnt))
