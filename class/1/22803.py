from itertools import permutations
matrix = '457 567 45 136 123 247 126'.split()
graf ='ef fa ab bg ge ec cb cd fd da'.split()
print(*range(1,8))
for i in permutations('efabgcd'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graf):
        print(*i)