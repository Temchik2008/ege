with open('24.txt') as f:
    s = f.readline()

s = s.replace('2025', '*')

ans = 0

for l in range(len(s)):
    cntY = 0
    cntStar = 0

    for r in range(l, n):
        if s[r] == 'Y':
            cntY += 1
        if s[r] == '*':
            cntStar += 1

        if cntY > 80:
            break

        if cntY == 80 and cntStar >= 90:
            ans = max(ans, r - l + 1)

print(ans)