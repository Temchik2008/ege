from itertools import product

alph = sorted('январь')
last = 0


for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[0] != 'я' and val.count('ь') <=1 and 'яя' not in val:
        last = pos
print(last)