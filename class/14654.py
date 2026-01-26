from itertools import combinations


def f(x):
    p = 43 <= x <= 49
    q = 44 <= x <= 53
    a = a1 <= x <= a2
    return (a <= p ) or q


linea = [43, 44, 49, 53]
linex = [43.5, 45, 50]
ans = []

for a1, a2 in combinations(linea, 2):
    if all(f(x) for x in linex):
        ans.append(a2 - a1)
print(max(ans))
