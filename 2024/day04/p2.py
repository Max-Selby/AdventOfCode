data = []
for line in open("data.txt", "r").readlines() :
    line = line.strip()
    data.append(line)

total = 0

# test = []
# for i in range(len(data)) :
#     add = []
#     for j in range(len(data[0])) :
#         add.append(".")
#     test.append(add)

def masStartsHere(mascomb, idx, jdx) :
    if idx + 3 > len(data) or jdx + 3 > len(data[0]) :
        return False
    if data[idx + 1][jdx + 1] == "A" and data[idx + 0][jdx + 0] == mascomb[0] and data[idx + 2][jdx + 0] == mascomb[1] and data[idx + 2][jdx + 2] == mascomb[2] and data[idx + 0][jdx + 2] == mascomb[3] :
        return True

for idx, line in enumerate(data) :
    for jdx, cha in enumerate(line) :
        for mas in [("M", "M", "S", "S"), ("M", "S", "S", "M"), ("S", "M", "M", "S"), ("S", "S", "M", "M")] : 
            if masStartsHere(mas, idx, jdx) :
                total += 1

                # test[idx + 1][jdx + 1] = "A"
                # test[idx + 0][jdx + 0] = mas[0] 
                # test[idx + 2][jdx + 0] = mas[1]
                # test[idx + 2][jdx + 2] = mas[2]
                # test[idx + 0][jdx + 2] = mas[3]

            
# for l in test :
#     for j in l :
#         print(j,end="")
#     print()
print(total)

# uncomment all the test lines to see a visualization!