rules = []
orderings = []
data = open("data.txt", "r").read()
data = data.split("\n\n")
for line in data[0].split("\n") :
    a, b = line.split("|")
    rules.append((int(a), int(b)))
for line in data[1].split("\n") :
    listt = []
    for part in line.split(",") :
        listt.append(int(part))
    orderings.append(listt)

totalMiddles = 0

def fixandgetmiddle(order) :
    newOrder = []
    remaining = []
    for i in order :
        remaining.append(i)
    while remaining != [] :
        for idx, page in enumerate(remaining) : 
            works = True
            for wantAfter in remaining :
                if (wantAfter, page) in rules :
                    works = False
                    break
            if works :
                newOrder.append(page)
                remaining = remaining[:idx] + remaining[idx+1:]
                break
    return newOrder[int(len(newOrder)/2)]


pagesPrinted = []
for order in orderings :
    failed = False
    for page in order :
        ok = True
        for before in pagesPrinted :
            if (page, before) in rules :
                ok = False
                break
        pagesPrinted.append(page)
        if not ok :
            failed = True
            break
    if failed :
        totalMiddles += fixandgetmiddle(order)
    pagesPrinted = []

print(totalMiddles)