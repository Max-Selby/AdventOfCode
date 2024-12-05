data = open("data.txt", "r").readlines()

total = 0

zL = []
zR = []
for idx, line in enumerate(data) :
    left = int(line.split(" ")[0])
    right = int(line.split(" ")[::-1][0])
    zL.append(left)
    zR.append(right)

for l in zL :
    total += l * zR.count(l)

print(total)
