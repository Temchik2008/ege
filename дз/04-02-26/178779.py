def f(num):
    d = set()
    for i in range(2, int(num**.5)+1):
        if num %i == 0:
            d |= {i, num//i}
    if d:
        cnt = max(d) + min(d)
        if cnt %10 == 4:
            return cnt
    return 0
cnt = 0

for num in range(800_001, 10000000):
    if x := f(num):
        print(num, x)
        cnt +=1
    if cnt == 5:
        break