def f(num):
    cnt  = 1
    dell = 1
    for i in range(2, int(num**.5)+1):
        if num% i == 0:
            cnt += i + (num//i)
            dell += 2
    con = cnt // dell
    if str(con)[-2:] == '12':
        return con
    return  0
cnt = 0
for num in range(1, 770000)[::-1]:
    if x := f(num):
        cnt +=1
        print(num, x)
    if cnt == 5:
        break
