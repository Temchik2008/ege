def dell(n, m):
    return n % m == 0

def f(x):
    return not (dell(x,263) <= dell(x, a)) and dell(x, 71)

for a in range(1, 10000)[::-1]:
    if all(not f(x) for x in range(1, 1000)):
        print(a)
        break