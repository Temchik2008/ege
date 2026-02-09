def prime(num):
    if num < 2: return False
    for i in range(2, int(num**.5)+1):
        if num % i ==0:
            return False
    return True

def f(x):
    d = []
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            if prime(i): d += [i]
            if prime(x // i): d += [x // i]
    if len(d)>= 2 :
        cnt = max(d) + min(d)
        if cnt>2000 and str(cnt)[-1:] == '8':
            return str(cnt)
    return 0
c =0
for num in range(1_200_001, 100000000000):
    if x := f(num):
        c +=1
        print(num, x)
    if c == 5:
        break

