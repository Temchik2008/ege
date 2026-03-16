from itertools import *

alph = sorted('аргумент')

for pos, val in enumerate(product(alph, repeat = 4), start = 1):
    if len(val) == len(set(val)):
        if list(val) == sorted(val):
            print(pos)