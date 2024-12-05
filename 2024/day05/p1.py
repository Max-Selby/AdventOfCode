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
    if not failed :
        totalMiddles += order[int(len(order)/2)]
    pagesPrinted = []

print(orderings)
print(totalMiddles)