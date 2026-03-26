with open('') as file:
    data= [list(map(int, i.split())) for i in file]

for pos, line in enumerate(data):
    cnt = [line.count(i) for i in set(line)]
    if sorted(cnt) == [1, 1, 1, 2, 2]:
        pov = [i for i in line if line.count(i) > 1]
        n = [i for i in line if %2 != 0]
        if sum(pov)