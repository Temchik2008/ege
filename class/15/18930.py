from itertools import combinations

def f(x):
    p = 10 <= x <= 150
    q = 160 <= x <= 250
    r = 240 <= x <= 300
    a = a1 <= x <= a2
    return (q <= p) or ((not a) <= r)

line = [10, 150, 160, 240, 250, 300]
lineb = [11, 151, 161, 241, 251]

ans = []

for a1, a2 in combinations(line, 2):
    if all(f(x) for x in lineb):
        ans.append(a2-a1)
print(min(ans))