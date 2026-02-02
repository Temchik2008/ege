from itertools import combinations
def DEL(n, m):
    return n%m == 0

def f(a):
    for x in range(1, 1000):
        f = (DEL(405, x) <= DEL(81, x)) or (a-x)>162
        if not f:
            return False
    return True

for a in range(1, 1000):
    if f(a):
        print(a)
        break