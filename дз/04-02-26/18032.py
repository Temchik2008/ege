def f(num):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0: cnt += i
    if str(cnt)[-2:] == '23' and cnt > 99:
        return cnt
    return 0
for num in range(1000, 10000):
    if x := f(num):
        print(num, x)
