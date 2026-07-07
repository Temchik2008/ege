def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            k = (2*x + y != 110) or (x<y) or (a < x)
            if not k:
                return False
    return True
ans = []
for a in range(1, 1000):
    if f(a):
        ans.append(a)
print(max(ans))
