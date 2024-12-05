data = open("data.txt", "r").readlines()

total = 0

for dat in data :
    a = dat.split(" ")
    numslist = []
    for b in a :
        numslist.append(int(b))
    passed1st = False
    passed2nd = True
    
    if numslist == sorted(numslist) or numslist == sorted(numslist, reverse=True) :
        passed1st = True

    
    for idx, item in enumerate(numslist) :
        if idx == 0 :
            continue
        if abs(item - numslist[idx-1]) > 3 or abs(item - numslist[idx-1]) == 0 :
            passed2nd = False
    if passed1st and passed2nd :
        total += 1


print(total)