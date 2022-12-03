#Advent of code Day-1
with open('day1.txt', "r") as file:
    content = file.read().split("\n")

max_snacks = 0
count_sum = 0
snacks = []
for i in content:
    if i == '':
        max_snacks = count_sum if count_sum > max_snacks else max_snacks
        snacks.append(int(count_sum))
        count_sum = 0
        continue
    count_sum += int(i)

print(f"Part 1: {max_snacks}")

snacks.sort(reverse=True)
print(f"Part 2: {snacks[0] + snacks[1] + snacks[2]}")
