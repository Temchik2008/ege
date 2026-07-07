with open('24_23281.txt') as file:
    data = file.readline()

patern = r'[2025]'

matches = [match.group() for match in finditer(patern, data)]
print(len(max(matches, key=len)))
