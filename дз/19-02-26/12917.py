from itertools import permutations

count = 0
for val in set(permutations('ПРОСТО')):
    val = ''.join(val)
    if 'ОО' not in val:
        count += 1

print(count)