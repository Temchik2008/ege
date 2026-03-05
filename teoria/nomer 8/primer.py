from re import finditer

with open(r'24_10724.txt') as file:
    data = file.readline()


pattern = r'[1-9A-F]+[0-9A-F]*'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))



from re import finditer

with open(r'24_18619.txt') as file:
    data = file.readline()


pattern = r'B[1-6]+([-\*][1-6]+)+'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))




from itertools import *

# permutations - формирует всевозможные перестановки элементов коллекции
alph_1 = '123'
for val_1 in permutations(alph_1):
    val = ''.join(val_1)
    print(val)

# product - формирует всевозможные комбинации определённой длинны
alph_2 = '123'
for val_2 in product(alph_2, repeat=3):
    val = ''.join(val_2)
    print(val)

# enumerate - нумерует элементы последовательности начиная от start
alph_3 = '123'
res = enumerate(alph_3, start=1)
print(*res)

def convert(num, x):
    val = 0
    for i in num:
        val = val * x + int(i, 36)
    return val


for p in range(33, 100):
    num1 = convert('KOT', p)
    num2 = convert('GOLODNI', p)
    num3 = convert('MEEOW', p)
    num4 = convert('100', p)
    if num1 + num2 == num3 * num4 - 20194023088:
        print(convert('PURR', p))
        