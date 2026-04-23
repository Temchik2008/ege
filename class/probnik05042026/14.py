from string import printable
n1 =int(39**483)
n2 = int(39**235)
res = n1 +n2
s =[]
for x in range(1, 9431):
    cnt = 0
    res = res - x
    for i in str(res):
        if i == '0':
            cnt +=1
    s.append(cnt)
print(max(s))


