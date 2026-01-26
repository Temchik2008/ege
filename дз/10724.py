with open('24_10724 (1).txt') as file:
    data  = file.readline()
x = '1234567890ABCDEF'
ans = ''
cnt = []
y = 0
for i in data:
    if i in x:
        ans += i
    else:
        cnt.append(ans)
for i in cnt:
    if i[0] != '0':
        y += 1
print(y)
