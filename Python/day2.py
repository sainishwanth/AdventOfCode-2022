with open('day2.txt', "r") as file:
    content = file.read().split("\n")

score = 0

for i in content:
    try:
        p1 = i[0]
        p2 = i[2]
    except:
        continue
    if p1 == 'A':
        if p2 == 'X':
            score += 1 + 3
        elif p2 == 'Y':
            score += 2 + 6
        elif p2 == 'Z':
            score += 3 + 0
    elif p1 == 'B':
        if p2 == 'X':
            score += 1 + 0
        elif p2 == 'Y':
            score += 2 + 3
        elif p2 == 'Z':
            score += 3 + 6
    elif p1 == 'C':
        if p2 == 'X':
            score += 1 + 6
        elif p2 == 'Y':
            score += 2 + 0
        elif p2 == 'Z':
            score += 3 + 3


print(f"Part 1: {score}")

score = 0
for j in content:
    try:
        p1 = j[0]
        p2 = j[2]
    except:
        continue
    
    if p1 == 'A':
        if p2 == 'X':
            score += 0 + 3
        elif p2 == 'Y':
            score += 3 + 1
        elif p2 == 'Z':
            score += 6 + 2
    elif p1 == 'B':
        if p2 == 'X':
            score += 0 + 1
        elif p2 == 'Y':
            score += 3 + 2
        elif p2 == 'Z':
            score += 6 + 3
    elif p1 == 'C':
        if p2 == 'X':
            score += 0 + 2
        elif p2 == 'Y':
            score += 3 + 3
        elif p2 == 'Z':
            score += 1 + 6

print(f"Part 2: {score}")
