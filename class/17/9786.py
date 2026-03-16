with open('') as file:
    data = [int(i) for i in file]

max = (i for i in data if abs(i) % 100 == 25)
for num1, num2, num3 in zip(data,  data[2:], data[3:]):
    if:

