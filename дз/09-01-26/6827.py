from itertools import combinations

def f(x):
    p = 257 <= x <= 1000
    q = 5 <= x <= 100
    r = 99 <= x <= 258
    a = a1 <= x <= a2
    return (a <= r) and (not(a <= p) <= q)

line = [13, 17, 19, 23]
lineb = [14, 18, 20]

ans = []

for a1, a2 in combinations(line, 2):
    if all(f(x) for x in lineb):
        ans.append(a2-a1)
print(min(ans))