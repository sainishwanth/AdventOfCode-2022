with open('day4.txt', 'r') as file:
    content = file.read().splitlines()

str = ''

count = 0

for i in content[0:10]:
    str = i
    r1, r2 = i.split(",", 1)
    r11, r12 = (r1.split("-", 1))
    r21, r22 = (r2.split("-", 2))
    r11, r12 = int(r11), int(r12)
    r21, r22 = int(r21), int(r22)
    print(f"elf 1 - {r11}-{r12}")
    print(f"elf 2 - {r21}-{r22}")
    xset = set(range(r11,r12+1))
    yset = set(range(r21,r22+1))
    x_inter_y = xset.update(yset)
    print(x_inter_y)
    if len(x_inter_y) == len(xset):
        count += 1

print(count)

      
