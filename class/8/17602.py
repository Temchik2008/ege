from string import printable
from itertools import *
cnt = 0

for val in product(printable[:14], repeat = 5):
    val = ''.join(val)
    if val.count('9') == 1 and val.count('b') +val.count('c') + val.count('d') <= 3 and val[0] != '0':
        cnt += 1
print(cnt)