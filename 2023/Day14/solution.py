
from enum import Enum


def getInput(filename):
    with open(filename, "r") as f:
        data = f.read()
        return data



def part1(filename):
    rocks = [list(x) for x in getInput(filename).splitlines()]
    total = 0
    for i in range(len(rocks)):
        for j in range(len(rocks[0])):
            currRow = i
            if(rocks[i][j] == "O"):
                rocks[i][j] = "."
                while (currRow > 0 and rocks[currRow-1][j] == "."):
                    currRow -= 1
                rocks[currRow][j] = "O"
                total += len(rocks) - currRow

    return total




class dir(Enum):
    NORTH = 1
    WEST = 2
    SOUTH = 3
    EAST = 4
    NONE = -1


def move(row, col, direction):
    if(direction == dir.NORTH):
        return row-1, col
    elif(direction == dir.WEST):
        return row, col-1
    elif(direction == dir.SOUTH):
        return row+1, col
    elif(direction == dir.EAST):
        return row, col+1
    else:
        return row, col


def isValid(row, col, rows, cols):
    return (row >= 0 and col >= 0 and
            row < rows and col < cols)


def roll(rocks, direction):
    rowIters = range(len(rocks))
    colIters = range(len(rocks[0]))
    if(direction == dir.SOUTH): rowIters = reversed(rowIters)
    # casted to list because you can only use a reversed range once before it stops working.
    # Wait what??? why??? this cost me like half an hour whyyyy
    if(direction == dir.EAST): colIters = list(reversed(colIters))

    for i in rowIters:
        for j in colIters:
            if(rocks[i][j] == "O"):
                rocks[i][j] = "."
                currRow, currCol = i, j
                nextRow, nextCol = move(currRow, currCol, direction)
                while (isValid(nextRow, nextCol, len(rocks), len(rocks[0])) and
                       rocks[nextRow][nextCol] == "."):
                    currRow, currCol = nextRow, nextCol
                    nextRow, nextCol = move(currRow, currCol, direction)
                rocks[currRow][currCol] = "O"

    return rocks




def cycle(rocks):
    rocks = roll(rocks, dir.NORTH)
    rocks = roll(rocks, dir.WEST)
    rocks = roll(rocks, dir.SOUTH)
    rocks = roll(rocks, dir.EAST)
    return rocks



def print2DArray(arr):
    for row in arr:
        print(''.join(row))


seenPositions = []
def part2(filename):
    rocks = [list(x) for x in getInput(filename).splitlines()]
    rocks = cycle(rocks)

    remainingCycles = 1_000_000_000
    position = ' '.join([''.join(x) for x in rocks])
    while position not in seenPositions:
        seenPositions.append(position)
        rocks = cycle(rocks)
        position = ' '.join([''.join(x) for x in rocks])
        remainingCycles -= 1
    
    cycleStart = seenPositions.index(position)
    cycleLength = len(seenPositions) - cycleStart

    remainingCycles %= cycleLength
    # why one? good question. I probably fucked something up earlier but it works like this. I dont ask.
    while remainingCycles > 1:
        rocks = cycle(rocks)
        remainingCycles -= 1
    
    total = 0
    for i in range(len(rocks)):
        for j in range(len(rocks[0])):
            if(rocks[i][j] == "O"): total += len(rocks) - i

    return total



def main():
    print("part 1:", part1("input.txt"))
    print("part 2:", part2("input.txt"))

if(__name__ == "__main__"):
    main()