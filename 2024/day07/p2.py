lines = open("data.txt", "r").read().split("\n")

def couldWork(out, current, inputs) :
    if inputs == [] :
        return out == current

    if len(inputs) != 1 :
        first = couldWork(out, current * inputs[0], inputs[1:])
        second = couldWork(out, current + inputs[0], inputs[1:])
        third = couldWork(out, int(str(current) + str(inputs[0])), inputs[1:])
    else :
        first = couldWork(out, current * inputs[0], [])
        second = couldWork(out, current + inputs[0], [])
        third = couldWork(out, int(str(current) + str(inputs[0])), [])

    return first or second or third

total = 0
for line in lines :
    out, inn = line.split(": ")
    out = int(out)
    inn = [int(x) for x in inn.split(" ")]
    assert len(inn) > 1
    if couldWork(out, inn[0], inn[1:]) :
        total += out

print(total)