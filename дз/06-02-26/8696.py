def prime(num):
    if num <2 : return False
    for i in range(2, int(num**.5)+1):
        if num %i == 0: return 0
    return True


def f(num):
    d = set()
    for i in range(2,int(num ** .5) +1):
        if num % i == 0:
            d |= {i, num//i}
    if prime(sum(d)):
        return []
    if prime(sum(d)%100_000):
        return [num, sum(d)]
    return []
cnt = 0
for n in range(1_273_548, 10**20):
    if m := f(n):
        print(*m)
        cnt +=1
        if cnt == 5:
            break