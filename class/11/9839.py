from math import ceil, log2
for l in range(1, 100 ** 6):
    n = 172
    i = ceil(log2(n))
    I = ceil(l * i/ 8)
    if I * 356984 > 54 *2 **20