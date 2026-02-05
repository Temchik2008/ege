def is_prime(num):
    if num <2 : return False
    for i in range(2, int(num**.5)+1):
        if num % i == 0:
            return 0
    return True

def fact(num):
    d = []
    i = 3
    while i < int(num ** .5) + 1:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]
    return d

cnt = 0
for n in range(5_000_001, 10**10, 2):
    dels = fact(n)
    if len(dels) == 2 and dels[0] != dels[1]:

        if is_prime(dels[1]- dels[0]):
            print(n, max(dels))
            cnt += 1
            if cnt == 5:
                break