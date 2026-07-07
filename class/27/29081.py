from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open('') as file:
    dots = []
    stars = []
    for i in file:
        x, y, info = i.replace(',', '.').split()
        dots.append([float(x), float(y)])
        if info == 'VII':
            stars.append(dots[-1])

cluster1 = [d for d in dots if d[1] <8 ]
cluster2 = [d for d in dots if 8 < d[1]]

stars1 = [d for d in stars if d[1] <8 ]
stars2 = [d for d in stars if 8 < d[1]]

center1 = center(cluster1)
center2 = center(cluster2)

a = []
for s in stars1:
    a.append(dist(center1, s))

for s in stars2:
    a.append(dist(center2, s))

print(min(a)*10_000, max(a)*10_000)


b1 = []

for s1 in stars1:
    for s2 in stars2:
        b1.append(dist(s1, s2))
for s1 in stars2:
    for s2 in stars2:
        b1.append(dist(s1, s2))
for s1 in stars2:
    for s2 in stars2:
        b1.append(dist(s1, s2))

b2 = []

for s1 in stars1:
    for s2 in stars1:
        if s1 != s2:
            b2.append()
