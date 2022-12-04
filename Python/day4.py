with open('/Users/sainishwanth/Documents/College/Coding/AdventOfCode2022/Python/day4.txt', 'r') as file:
    content = file.read().splitlines()

str = ''

count = 0

for i in content:
    str = i
    r1, r2 = i.split(",", 1)
    r11, r12 = (r1.split("-", 1))
    r21, r22 = (r2.split("-", 2))
    r11, r12 = int(r11), int(r12)
    r21, r22 = int(r21), int(r22)
    l1 = [j for j in range(r11,r12+1)]
    l2 = [k for k in range(r21,r22+1)]
    similar = []
    for j1 in l1:
        if j1 in l2:
            similar.append(j1)
    if similar == l1:
        count += 1
        continue
    elif similar == l2:
        count += 1
    
    

print(count)

      
