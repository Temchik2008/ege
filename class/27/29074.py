from math import dist

def cntr(clust):
    res = []
    for dot in clust:
        sum_dist = [dist(dot, d) for d in clust]
        res.append([sum_dist, dot])
    return min(res)[1]

with open('27_A_29074.txt') as file:
    dots = []
    target =[]
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Z':
            target.append(list(map(float, [x,y])))

cl1 = [d for d in dots if d[1] < 8 ]
cl2 = [d for d in dots if d[1] > 8]

tg1 = [d for d in target if d[1] < 8 ]
tg2 = [d for d in target if d[1] > 8 ]

print(len(tg1))
print(len(tg2))