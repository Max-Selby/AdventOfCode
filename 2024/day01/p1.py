data = open("data.txt", "r").readlines()

total = 0

zL = []
zR = []
for idx, line in enumerate(data) :
    left = int(line.split(" ")[0])
    right = int(line.split(" ")[::-1][0])
    zL.append(left)
    zR.append(right)

zL.sort()
zR.sort()

for l, r in zip(zL, zR) :
    total += abs(l - r)

print(total)
