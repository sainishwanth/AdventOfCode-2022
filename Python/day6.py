with open('day6.txt', 'r') as file:
    content = file.read()
temp = 4
string4 = ''
for i in range(0,len(content)):
    string4 = content[i:temp]
    if len(set(string4)) == len(string4):
        break
    temp += 1

print(f"Part 1: {temp}")
print(string4)

temp = 14
string14 = ''
for i in range(0,len(content)):
    string14 = content[i:temp]
    if len(set(string14)) == len(string14):
        break
    temp += 1
print(f"Part 2: {temp}")
print(string14)
    
    