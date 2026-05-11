with open('') as file:
    data = file.readline()

ans = 0

for i in range(len(data)-1):
    if i < new_start:
        continue
    if data[i:i + 2] in 'AB AC':
        cnt = 1
        for j in range(i + 2, len(data) -1, 2):
            if data[j:j + 2] in 'AB AC':
                cnt += 1
            else:
                new_start = j
                break
        ans = max(ans, cnt)
print(ans)

#метод скользящего окна

with open('') as file:
    data = file.readline()

ans = cnt = i = 0
while i < len(data) - 1:
    if data[i:i +2] in 'AB AC':
        cnt +=1
        i += 3
    else:
        cnt = 0
        i += 1
    ans = max(ans, cnt)
print(ans)

with open('') as file:
    data = file.readline()

ans = cnt = i = 0

while i < len(data) - 1:
    if data[i:i +2] in 'AB AC':
        cnt +=1
        i += 2
    else:
        cnt = 0
        i += 1
    ans = max(ans, cnt)
print(ans)

#1975

with open('') as file:
    data = file.readline()

ans = i = 0
cnt = 1

while i < len(data) - 1:
    if not(data[i:i +2] in 'PP'):
        cnt +=1
    else:
        cnt = 1
    i += 1
    ans = max(ans, cnt)
print(ans)

#type 3 9753

with open('') as file:
    data = file.readline()

data = data.split('Y')

ans = 0
for i in range(len(data) - 150 ):
    line = 'Y'.join(data[i:i + 151])
    ans = max(ans, len(line))

print(ans)

#9753 скользщие окно

with open('') as file:
    data = file.readline()

ans = cnt = l = r = 0

while r < len(data):
    if cnt <= 150:
        if data[r] == 'Y': cnt +=1
        r += 1
    else:
        if data[l] == 'Y': cnt -=1
        l+=1
    ans = max(ans, r - l - 1)


#type 4

from re import finditer

with open('') as file:
    data = file.readline()

patern = r'[1-9AB][0-9AB]*[02468A]'

matches = [match.group() for match in finditer(patern, data)]
print(len(max(matches, key=len)))


from string import printable

with open('') as file:
    data = file.readline().lower()

for i in printable[16:]:
    data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))


with open('') as file:
    data = file.readline().lower()

for i in printable[12:36]:
    data = data.relace(i, ' ')

data = data.split()

print(len(max([i.lsrip('0').rstrip('13579b') for i in data], key = len)))




from re import finditer

with open('24_23206.txt') as file:
    data = file.readline()

patern = r'[2468]([^S02468]*S){35}[^S02468]*'

matches = [match.group() for match in finditer(patern, data)]
print(len(max(matches, key=len)))


with open('') as file:
    data = file.readline()

data = data.split('AB', 'A B')
data = data.split()

ans = 0
for i in range(len(data) - 100 ):
    line = ''.join(data[i:i + 101])
    ans = max(ans, len(line))

print(ans)


























