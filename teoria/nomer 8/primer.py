from itertools import product

def f(val):
    for x in range(1, 10, 2):
        val = val.replace(str(x), '*')
    for y in range(0, 10, 2):
        val = val.replace(str(y), '/')
    for i in range(len(val)-1):
        if val[i] == val[i+1]:
            return False
    return True

alph = '0234567'

cnt = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if len(val) == len(set(val)) and f(val) and val[0] != '0':
            cnt +=1
print(cnt)
