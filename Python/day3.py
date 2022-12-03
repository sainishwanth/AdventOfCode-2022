# Advent of Code - Day 3
with open('day3.txt', 'r') as file:
    content = file.read().splitlines()

def charValue(char):
    if ord(char) >= 97 and ord(char) <= 122:  #Lowercase
        return ord(char)-96
    elif ord(char) >= 65 and ord(char) <= 90:  #Uppercase
        return ord(char)-38

sum = 0

for i in content:
    partition = int((len(i)) / 2)
    string1, string2 = i[0:partition], i[partition: len(i)]
    for j in string1:
        if j in string2:
            break
    sum += charValue(j)

print(f"Part 1: {sum}")

sum = 0

for i in range(0, len(content), 3):
    string1, string2, string3 = content[i], content[i+1], content[i+2]
    for j in string1:
        if j in string2 and j in string3:
            break
    sum += charValue(j)

print(f"Part 2 : {sum}")
