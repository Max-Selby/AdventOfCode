data = open("data.txt", "r").readlines()

total = 0

def isSafe(numslist) :
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
        return True
    return False

for dat in data :
    a = dat.split(" ")
    numslist = []
    for b in a :
        numslist.append(int(b))
    good = False
    if isSafe(numslist) :
        good = True
    else :
        for idx, item in enumerate(numslist) :
            if isSafe(numslist[:idx] + numslist[idx + 1:]) :
                good = True
    if good :
        total += 1


print(total)