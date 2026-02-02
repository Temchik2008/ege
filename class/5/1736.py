ans = []
for n in range(1,1000):
    r = int(''.join([i + i for i in f'{n:b}']), 2)
    if r > 63:
        ans.append(r)
print(min(ans))
