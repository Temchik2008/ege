
from itertools import combinations

def f(x):
    b =  80 <= x <= 100
    a = a1<= x <= a2
    return (x%17 == 0) <= ((not b) or (a<x +30))


linea = [80, 100]
linex = [90]

ans = []

for a1, a2 in combinations(linea, 2):
    if all( f(x) for x in linex):
        ans.append(a2 - a1)
print(max(ans))