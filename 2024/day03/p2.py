data = open("data.txt", "r").read()

total = 0
toggle = True
for i in range(len(data)) :
    if data[i:].startswith("do()") :
        toggle = True
    elif data[i:].startswith("don't()") :
        toggle = False
    elif toggle == True and data[i:].startswith("mul(") and data[i:].find(")") <= len("mul(123,123)") and data[i:].find(")") != -1 :
            try :
                cmd = data[i:].split("(")[1].split(")")[0]
                l, r = cmd.split(",")
                total += int(l) * int(r)
            except :
                pass

print(total)