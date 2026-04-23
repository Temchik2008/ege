from itertools import permutations
matrix = '457 567 45 136 123 247 126' .split()
graf = 'ge ef fa bg ec cb cd df da'.split()
for i in permutations('gefabdc'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graf):
        print(*i)