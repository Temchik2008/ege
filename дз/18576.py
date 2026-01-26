from itertools import permutations, product

def f(x, y, w, z):
    return not(w <= (x == y )) and (z<=x)

for i in product((0,1), repeat =5):
    tabele = [
        (i[0], 1, 1, i[1]),
        (0, i[2], i[3], 0),
        (i[4], 0,1,0)
    ]
    for p in permutations('xywz'):
        if [f(**dict(zip(p, t))) for t in tabele] == [1,1,1]:
            print(*p)