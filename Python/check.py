with open('/Users/sainishwanth/Documents/College/Coding/AdventOfCode2022/Python/day5.txt', 'r') as file:
    content = file.read().splitlines()

print(int(content[0][17:19].strip()))

s1 = ['P', 'L', 'M', 'N', 'W', 'V', 'B', 'H']
print(s1.pop())
print(s1)