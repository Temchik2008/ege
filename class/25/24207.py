from math import prod
def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def f(x):
    d = []
    for i in range(2, int(x ** .5)+ 1):
        if x % i ==0:
            if is_prime(i): d +=[i]
            if is_prime(x//i): d += [x//i]
    if len(d) > 11 and prod(d) == x:
        return max(d)
    return 0

cnt = 0
for n in range(24517512+1, 10**20):
    if m := f(n):
        print(n, m)
        cnt +=1
        if cnt == 5:
            break


