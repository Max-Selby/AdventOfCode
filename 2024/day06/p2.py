grid = open("data.txt", "r").read().split("\n")

visitedNoStart = set()

def findGuard() :
    for idx, elem in enumerate(grid) :
        for jdx, letter in enumerate(elem) :
            if letter == "^" :
                return (jdx, idx)
            
def cloneGrid() :
    clone = []
    for i in grid :
        c = ""
        for j in i :
            c += j
        clone.append(c)
    return clone

pos = findGuard()
startPos = findGuard()
dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
direction = (0, -1)

while -1 < pos[0] < len(grid[0]) and -1 < pos[1] < len(grid) :
    visitedNoStart.add(pos)
    canWalk = True
    try :
        if grid[pos[1] + direction[1]][pos[0] + direction[0]] == "#" :
            canWalk = False
            direction = dirs[(dirs.index(direction) + 1) % 4]
    except :
        pass
    if canWalk :
        pos = (pos[0] + direction[0], pos[1] + direction[1])
visitedNoStart.remove(startPos)

total = 0
for position in visitedNoStart : 
    grid2 = cloneGrid()
    grid2[position[1]] = grid2[position[1]][:position[0]] + "#" + grid2[position[1]][position[0]+1:]
    pos = findGuard()
    direction = (0, -1)
    visited = set()
    
    iter = 0
    while -1 < pos[0] < len(grid2[0]) and -1 < pos[1] < len(grid2) :
        if (pos, direction) in visited :
            total += 1
            break
        visited.add((pos, direction))
        canWalk = True
        try :
            if grid2[pos[1] + direction[1]][pos[0] + direction[0]] == "#" :
                canWalk = False
                direction = dirs[(dirs.index(direction) + 1) % 4]
        except :
            pass
        if canWalk :
            pos = (pos[0] + direction[0], pos[1] + direction[1])
        iter += 1

print(total)