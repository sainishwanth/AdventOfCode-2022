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
    string1 = i[0:partition]
    string2 = i[partition: len(i)]
    for j in string1:
        for k in string2:
            if j == k:
                common_char = k
                break
    sum += charValue(common_char)    

print(f"Part 1: {sum}")

sum = 0

for i in range(0, len(content), 3):
    string1 = content[i]
    string2 = content[i+1]
    string3 = content[i+2]
    for j in string1:
        for k in string2:
            if j == k:
                for l in string3:
                    if j == l:
                        common_char = l
                        break
    sum += charValue(common_char)

print(f"Part 2 : {sum}")
