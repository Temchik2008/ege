with open('24_11667.txt') as file:
    d = file.readline()
d = d.split('INFINITY')
ans = 0
for i in range(len(d) - 1000):
    if i == 0 or i == len(d) - 1001:
        ans = max(ans, len('INFINITY'.join(d[i:i + 1001])) + 7)
    else:
        ans = max(ans, len('INFINITY'.join(d[i:i + 1001])) + 14)
print(ans)
