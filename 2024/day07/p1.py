lines = open("data.txt", "r").read().split("\n")

def couldWork(out, inputs) :
    makers = []
    assert len(inputs) != 1
    for binn in range(2 ** (len(inputs) - 1)) :
        binn = bin(binn)[2:]
        binn = "0" * ((len(inputs) - 1) - len(binn)) + binn
        makers.append(binn)

    for maker in makers :
        su = inputs[0]
        for idx, inpu in enumerate(inputs[1:]) :
            if maker[idx] == "0" :
                su = su * inpu
            else :
                su = su + inpu
        if su == out :
            return True
    return False

total = 0
for line in lines :
    out, inn = line.split(": ")
    out = int(out)
    inn = [int(x) for x in inn.split(" ")]
    if couldWork(out, inn) :
        total += out

print(total)