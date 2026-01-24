from turtle import *

screensize (3000, 3000)
tracer(False)
m= 15


fd(30*m)
lt(60)
fd(24*m)
rt(240)

fd(54*m)
lt(120)
fd(24*m)
lt(60)

up()

fd(30*m)
rt(90)
fd(20*m)

down()

for i in range(1, 17):
    fd(6*m)
    lt(90)
    fd(80*m)
    rt(90)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*m, y*m)
        dot(3, 'red')
update()
done()
