with open('17_28762.txt') as file:
    data = [int(i) for i in file]
min23= min(i for i in data if i% 23== 0)

ans = []

for nums in zip(data, data[1:]):
    if nums[0]%min23== 0 or nums[1]%min23== 0:
        ans.append(sum(nums))
print(len(ans), max(ans))
