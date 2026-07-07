with open('17_29349.txt') as file:
    data = [int(i) for i in file]

min123 = min(i for i in data if abs(i) % 123 == 0 and i > 0)

ans = []

for nums in zip(data, data[1:]):
    if sum(nums) < min123:
        ans.append(sum(nums))
print(len(ans), max(ans))