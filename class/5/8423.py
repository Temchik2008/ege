ans = []
for n in range(1, 10000000):
    r = f'{n:b}'
    if n % 5 == 0:
        r += f'{5:b}'
    else:
        r += '1'
    if int(r, 2) % 7 == 0:
        r += f'{7:b}'
    else:
        r += '1'
    r = int(r, 2)
    if r < 1_855_663:
        ans.append(n)
print(max(ans))