from itertools import permutations

matrix = '367 568 18 58 247 127 156 234'.split()
graf = 'eh hg gc cf fa ae ed df db hb gb'. split()

print(*range(1, 9))

for i in permutations('aehgcfdb'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graf):
        print(*i)
print(10+ 11)