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
#    test.append(add)

def foundFVector(vector:tuple, idx, jdx) :
    s = "MAS"

    if  idx + (3 * vector[0]) < 0 or jdx + (3 * vector[1]) < 0 :
        return False
    
    try :
        one = data[idx + (1 * vector[0])][jdx + (1 * vector[1])] == s[0]
        two = data[idx + (2 * vector[0])][jdx + (2 * vector[1])] == s[1]
        thr = data[idx + (3 * vector[0])][jdx + (3 * vector[1])] == s[2]
        if one and two and thr :
            return True
    except :
        return False
    return False

for idx, line in enumerate(data) :
    for jdx, cha in enumerate(line) :
        if cha == "X" :
            for vector in [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)] : 
                if foundFVector(vector, idx, jdx) :
                    total += 1

                    # test[idx][jdx] = "X"
                    # test[idx + (1 * vector[0])][jdx + (1 * vector[1])] = "M"
                    # test[idx + (2 * vector[0])][jdx + (2 * vector[1])] = "A"
                    # test[idx + (3 * vector[0])][jdx + (3 * vector[1])] = "S"
            
# for l in test :
#     for j in l :
#         print(j,end="")
#     print()
print(total)

# uncomment all the test lines to see a visualization!