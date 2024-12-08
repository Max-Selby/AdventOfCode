from itertools import combinations

map = open("data.txt", "r").read().split("\n")

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
        
        # start
        antinodes.add(combo[0])
        
        # direction 1
        i = 1
        while True :
            spot = (combo[0][0] + (xDiff * i), combo[0][1] + (yDiff * i))
            valid_spot = -1 < spot[0] < len(map[0]) and -1 < spot[1] < len(map)
            if valid_spot :
                antinodes.add(spot)
            else :
                break
            i += 1

        # direction 2
        i = 1
        while True :
            spot = (combo[0][0] - (xDiff * i), combo[0][1] - (yDiff * i))
            valid_spot = -1 < spot[0] < len(map[0]) and -1 < spot[1] < len(map)
            if valid_spot :
                antinodes.add(spot)
            else :
                break
            i += 1

print(len(antinodes))
