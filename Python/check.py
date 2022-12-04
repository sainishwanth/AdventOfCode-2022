r11 = 1
r12 = 5

r21 = 1
r22 = 5

l1 = [j for j in range(r11,r12+1)]
l2 = [k for k in range(r21,r22+1)]
print(l1)
l1.extend(l2)
s1 = set(l1)
s2 = set(l1)
print(len(s1))