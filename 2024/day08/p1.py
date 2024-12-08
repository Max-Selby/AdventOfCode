from itertools import combinations

map = open("test.txt", "r").read().split("\n")

antinodes = set()
nodesGroupsLocations = {}

for jdx, line in enumerate(map) :
    for idx, cha in enumerate(line) :
        if cha != "." :
            if not cha in nodesGroupsLocations :
                nodesGroupsLocations[cha] = set()
            s = nodesGroupsLocations[cha].add((idx,jdx))

for nodeKey in nodesGroupsLocations.keys() :
    combos = list(combinations(nodesGroupsLocations[nodeKey], 2))
    
    for combo in combos :
        xDiff = combo[0][0] - combo[1][0]
        yDiff = combo[0][1] - combo[1][1]
        for spot in [(combo[0][0] - xDiff, combo[0][1] - yDiff), (combo[0][0] + xDiff, combo[0][1] + yDiff), (combo[1][0] - xDiff, combo[1][1] - yDiff), (combo[1][0] + xDiff, combo[1][1] + yDiff)] :
            valid_spot = -1 < spot[0] < len(map[0]) and -1 < spot[1] < len(map)
            if spot != combo[0] and spot != combo[1] and valid_spot :
                antinodes.add(spot)

print(len(antinodes))
