from math import dist

def cntr(clust):
    res = []
    for dot in clust:
        sum_dist = [dist(dot, d) for d in clust]
        res.append([sum_dist, dot])
    return min(res)[1]

with open('') as file:
    dots = []
    target =[]
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Y' and data[2:] == 'III':
            target.append(list(map(float, [x,y])))

cl1 = [d for d in dots if d[1] < 8 ]
cl2 = [d for d in dots if d[1] > 8]
cl = [cl1, cl2]
min_cl = cntr(min(cl, key= len))
ans = [dist(min_cl, d) for d in target]
print(min(ans) * 10_000, max(ans) * 10_000)