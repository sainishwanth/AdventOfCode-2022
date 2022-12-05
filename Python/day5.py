# [P]     [L]         [T]            
# [L]     [M] [G]     [G]     [S]    
# [M]     [Q] [W]     [H] [R] [G]    
# [N]     [F] [M]     [D] [V] [R] [N]
# [W]     [G] [Q] [P] [J] [F] [M] [C]
# [V] [H] [B] [F] [H] [M] [B] [H] [B]
# [B] [Q] [D] [T] [T] [B] [N] [L] [D]
# [H] [M] [N] [Z] [M] [C] [M] [P] [P]
#  1   2   3   4   5   6   7   8   9 

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
    data = i.split()
    n = int(data[1])
    sfrom = stack_dict[int(data[3])]
    sto = stack_dict[int(data[5])]
    for i in range(0,n):
        sto.insert(0, sfrom.pop(0))

print("Part 1: ")
for j in stack_dict:
    print(stack_dict[j][0], end='')
print("\n")

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
    data = i.split()
    n = int(data[1])
    sfrom = stack_dict[int(data[3])]
    sto = stack_dict[int(data[5])]
    while n > 0:
        sto.insert(0, sfrom.pop(n-1))
        n -= 1

print("Part 2: ")
for j in stack_dict:
    print(stack_dict[j][0], end='')
        
    
    
