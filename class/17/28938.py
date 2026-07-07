with open('17_28938.txt') as file:
    data = [int(i) for i in file]

max28= max(i for i in data if abs(i)%100 == 28)
ans = []
for nums in zip(data, data[1:], data[2:]):
    if sum(len(str(abs(num))) == 3 for num in nums) >=1 and sum(nums) > 0:
        if sum(nums)/3< max28:
            ans.append(sum(nums))
print(len(ans), max(ans))