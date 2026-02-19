from itertools import permutations
matrix = '248 137 268 15 467 357 256 13'.split()
graf = 'гб бж же ев вд дг гк бк ка ае да'.split()
print(*range(1, 9))
for i  in permutations('гбжевдка'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graf):
        print(*i)
