from string import printable as alph
from itertools import *
cnt =0
for val in product(alph[:7], repeat= 7):
    val = ''.join(val)
    if val[0] != '3' and val[0] != '5':
        if ('22' not in val) and ('44' not in val):
            cnt += 1
print(cnt)
