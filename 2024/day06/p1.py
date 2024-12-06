grid = open("data.txt", "r").read().split("\n")

visited = set()

def findGuard() :
    for idx, elem in enumerate(grid) :
        for jdx, letter in enumerate(elem) :
            if letter == "^" :
                return (jdx, idx)
pos = findGuard()
dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
direction = (0, -1)

while -1 < pos[0] < len(grid[0]) and -1 < pos[1] < len(grid) :
    visited.add(pos)
    canWalk = True
    try :
        if grid[pos[1] + direction[1]][pos[0] + direction[0]] == "#" :
            canWalk = False
            direction = dirs[(dirs.index(direction) + 1) % 4]
    except :
        pass
    if canWalk :
        pos = (pos[0] + direction[0], pos[1] + direction[1])

print(len(visited))