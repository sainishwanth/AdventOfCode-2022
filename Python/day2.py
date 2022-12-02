with open('day2.txt', "r") as file:
    content = file.read().split("\n")

score = 0
score2 = 0
for i in range(0,len(content)-1):
    p1 = content[i][0]
    p2 = content[i][2]
    if p1 == 'A':
        if p2 == 'X':
            score += 1 + 3
            score2 += 0 + 3
        elif p2 == 'Y':
            score += 2 + 6
            score2 += 3 + 1
        elif p2 == 'Z':
            score += 3 + 0
            score2 += 6 + 2
    elif p1 == 'B':
        if p2 == 'X':
            score += 1 + 0
            score2 += 0 + 1
        elif p2 == 'Y':
            score += 2 + 3
            score2 += 3 + 2
        elif p2 == 'Z':
            score += 3 + 6
            score2 += 6 + 3
    elif p1 == 'C':
        if p2 == 'X':
            score += 1 + 6
            score2 += 0 + 2
        elif p2 == 'Y':
            score += 2 + 0
            score2 += 3 + 3
        elif p2 == 'Z':
            score += 3 + 3
            score2 += 1 + 6


print(f"Part 1: {score}")
print(f"Part 2: {score2}")
