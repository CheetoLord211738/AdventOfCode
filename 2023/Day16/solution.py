
from enum import Enum

def getInput(filename):
    with open(filename, "r") as f:
        data = f.read()
        return data


class direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    NONE = -1



def activePath(mirrors, energized, pos, dir):
    if(pos[0] >= len(mirrors) or pos[0] < 0): return False
    if(pos[1] >= len(mirrors[0]) or pos[1] < 0): return False
    if(mirrors[pos[0]][pos[1]] in "-|" and energized[pos[0]][pos[1]]): return False
    return True


def move(pos, dir):
    if(dir == direction.UP):
        return (pos[0]-1, pos[1])
    elif(dir == direction.DOWN):
        return (pos[0]+1, pos[1])
    elif(dir == direction.LEFT):
        return (pos[0], pos[1]-1)
    elif(dir == direction.RIGHT):
        return (pos[0], pos[1]+1)
    elif(dir == direction.NONE):
        return pos
    else:
        return (-1, -1)


def reflect(dir, mirror):
    if(mirror == "/"):
        if(dir == direction.UP): return direction.RIGHT
        if(dir == direction.DOWN): return direction.LEFT
        if(dir == direction.LEFT): return direction.DOWN
        if(dir == direction.RIGHT): return direction.UP
    else:
        if(dir == direction.UP): return direction.LEFT
        if(dir == direction.DOWN): return direction.RIGHT
        if(dir == direction.LEFT): return direction.UP
        if(dir == direction.RIGHT): return direction.DOWN


def followBeam(mirrors, energized, pos, dir):
    while(activePath(mirrors, energized, pos, dir)):
        energized[pos[0]][pos[1]] = True
        currCell = mirrors[pos[0]][pos[1]]

        if(currCell == "."):
            pos = move(pos, dir)

        elif(currCell in "\/"):
            dir = reflect(dir, currCell)
            pos = move(pos, dir)

        elif(currCell == "-"):
            if(dir == direction.LEFT or dir == direction.RIGHT):
                pos = move(pos, dir)
            else:
                newDir1 = reflect(dir, "\\")
                newPos1 = move(pos, newDir1)
                energized = followBeam(mirrors, energized, newPos1, newDir1)

                newDir2 = reflect(dir, "/")
                newPos2 = move(pos, newDir2)
                energized = followBeam(mirrors, energized, newPos2, newDir2)

                return energized
                
        elif(currCell == "|"):
            if(dir == direction.UP or dir == direction.DOWN):
                pos = move(pos, dir)
            else:
                newDir1 = reflect(dir, "\\")
                newPos1 = move(pos, newDir1)
                energized = followBeam(mirrors, energized, newPos1, newDir1)

                newDir2 = reflect(dir, "/")
                newPos2 = move(pos, newDir2)
                energized = followBeam(mirrors, energized, newPos2, newDir2)
                
                return energized
    return energized


def part1(filename):
    mirrors = getInput(filename).splitlines()
    energized = [[False for _ in range(len(mirrors[0]))] for _ in range(len(mirrors))]

    energized = followBeam(mirrors, energized, (0, 0), direction.RIGHT)

    return sum([len([y for y in x if y]) for x in energized])




def runSim(mirrors, pos, dir):
    energized = [[False for _ in range(len(mirrors[0]))] for _ in range(len(mirrors))]
    energized = followBeam(mirrors, energized, pos, dir)
    return sum([len([y for y in x if y]) for x in energized])


def part2(filename):
    mirrors = getInput(filename).splitlines()

    bestEnergized = 0

    for i in range(len(mirrors)):
        simResult = runSim(mirrors, (0, i), direction.DOWN)
        if(simResult > bestEnergized): bestEnergized = simResult

    for i in range(len(mirrors)):
        simResult = runSim(mirrors, (len(mirrors)-1, i), direction.UP)
        if(simResult > bestEnergized): bestEnergized = simResult
    
    for i in range(len(mirrors)):
        simResult = runSim(mirrors, (i, 0), direction.RIGHT)
        if(simResult > bestEnergized): bestEnergized = simResult

    for i in range(len(mirrors)):
        simResult = runSim(mirrors, (i, len(mirrors[0])-1), direction.LEFT)
        if(simResult > bestEnergized): bestEnergized = simResult

    return bestEnergized



def main():
    print("part 1:", part1("input.txt"))
    print("part 2:", part2("input.txt"))

if(__name__ == "__main__"):
    main()