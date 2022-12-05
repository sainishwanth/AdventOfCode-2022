with open('day5.txt', 'r') as file:
    content = file.read().splitlines()


s1 = ['P', 'L', 'M', 'N', 'W', 'V', 'B', 'H']
s2 = ['H', 'Q', 'M']
s3 = ['L', 'M', 'Q', 'F', 'G', 'B', 'D', 'N']
s4 = ['G', 'W', 'M', 'Q', 'F', 'T', 'Z']
s5 = ['P', 'H', 'T', 'M']
s6 = ['T', 'G', 'H', 'D', 'J', 'M', 'B', 'C']
s7 = ['R', 'V', 'F', 'B', 'N', 'M']
s8 = ['S', 'G', 'R', 'M', 'H', 'L', 'P']
s9 = ['N', 'C', 'B', 'D', 'P']

stack_dict = {1:s1, 2:s2, 3:s3, 4:s4, 5:s5, 6:s6, 7:s7, 8:s8, 9:s9}


for i in content:
    n = int(i[4:7].strip())
    from_ = int(i[12:14].strip())
    to_ = int(i[17:19].strip())
    sfrom = stack_dict[from_]
    sto = stack_dict[to_]
    for i in range(0,n):
        sto.insert(0, sfrom.pop(0))

print("Part 1: ")
for j in stack_dict:
    print(stack_dict[j][0], end='')
print("\n")
    
