with open('24var01.txt') as file:
    data = file.readline()

cnt = 0
cnt_data = 0

for i in range(1, 10, 2):
    data = data.replace('i', '*') 