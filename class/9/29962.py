with open(r'.\files\12241.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 2, 2, 2]:
        pov = [i for i in line if line.count(i) > 1]
        nepov = [i for i in line if line.count(i) == 1]
        if (min(pov) + max(pov)) / 2 < nepov[0]:
            cnt += 1
print(cnt)
