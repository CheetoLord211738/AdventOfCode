
from enum import Enum


def getInput(filename):
    with open(filename, "r") as f:
        data = f.read()
        return data



class direction(Enum):
    NONE = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


def rotateDir(dir, toLeft):
    if(dir == direction.NONE): return dir
    
    if(toLeft):
        if(dir == direction.UP): return direction.LEFT
        elif(dir == direction.LEFT): return direction.DOWN
        elif(dir == direction.DOWN): return direction.RIGHT
        elif(dir == direction.RIGHT): return direction.UP
    
    else:
        if(dir == direction.UP): return direction.RIGHT
        elif(dir == direction.RIGHT): return direction.DOWN
        elif(dir == direction.DOWN): return direction.LEFT
        elif(dir == direction.LEFT): return direction.UP
    
    return direction.NONE


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



def rotate(pipe, dir):
    if(pipe == "|" or pipe == "-"): #assume pipe was reached correctly
        return dir
    
    elif(pipe == "L"):
        if(dir == direction.DOWN): return direction.RIGHT
        if(dir == direction.LEFT): return direction.UP
        else: return direction.NONE
    
    elif(pipe == "J"):
        if(dir == direction.DOWN): return direction.LEFT
        if(dir == direction.RIGHT): return direction.UP
        else: return direction.NONE
    
    elif(pipe == "7"):
        if(dir == direction.RIGHT): return direction.DOWN
        if(dir == direction.UP): return direction.LEFT
        else: return direction.NONE
    
    elif(pipe == "F"):
        if(dir == direction.UP): return direction.RIGHT
        if(dir == direction.LEFT): return direction.DOWN
        else: return direction.NONE



def part1(filename):
    pipes = getInput(filename).splitlines()

    #find start location
    sLoc = None
    for i, row in enumerate(pipes):
        for j, char in enumerate(row):
            if(char == "S"):
                sLoc = (i, j)
    if(sLoc == None): return -1

    #find adjacent tile to start search from
    searchDirection = direction.NONE
    if(sLoc[0] > 0): #search up
        pipe = pipes[sLoc[0] - 1][sLoc[1]]
        if (pipe in "|F7"):
            searchDirection = direction.UP
    if(searchDirection == direction.NONE and sLoc[0] < len(pipes) - 1): #search down
        pipe = pipes[sLoc[0] + 1][sLoc[1]]
        if (pipe in "|JL"):
            searchDirection = direction.DOWN
    if(searchDirection == direction.NONE and sLoc[1] > 0): #search left
        pipe = pipes[sLoc[0]][sLoc[1] - 1]
        if (pipe in "-FL"):
            searchDirection = direction.LEFT
    if(searchDirection == direction.NONE and sLoc[1] < len(pipes[0]) - 1): #search right
        pipe = pipes[sLoc[0]][sLoc[1] + 1]
        if (pipe in "-J7"):
            searchDirection = direction.RIGHT
    
    if(searchDirection == direction.NONE): return -2

    #start traversing pipe
    pipePositions = [sLoc]
    currPos = move(sLoc, searchDirection)
    currDirection = searchDirection
    while(pipes[currPos[0]][currPos[1]] != "S"):
        pipePositions.append(currPos)

        pipe = pipes[currPos[0]][currPos[1]]
        currDirection = rotate(pipe, currDirection)
        currPos = move(currPos, currDirection)

    return len(pipePositions) // 2



#returns the rotated value, along with a boolean stating whether a left or right rotation occured (True == left)
def rotateAndIsLeft(pipe, dir):
    if(pipe == "|" or pipe == "-"): #assume pipe was reached correctly
        return dir, None
    
    elif(pipe == "L"):
        if(dir == direction.DOWN): return (direction.RIGHT, True)
        if(dir == direction.LEFT): return (direction.UP, False)
        else: return direction.NONE, None
    
    elif(pipe == "J"):
        if(dir == direction.DOWN): return (direction.LEFT, False)
        if(dir == direction.RIGHT): return (direction.UP, True)
        else: return direction.NONE, None
    
    elif(pipe == "7"):
        if(dir == direction.RIGHT): return (direction.DOWN, False)
        if(dir == direction.UP): return (direction.LEFT, True)
        else: return direction.NONE, None
    
    elif(pipe == "F"):
        if(dir == direction.UP): return (direction.RIGHT, False)
        if(dir == direction.LEFT): return (direction.DOWN, True)
        else: return direction.NONE, None

#flood fill from location
def claimPipes(claimedPipes, cyclePipes, startPos, searchDir):
    startPos = move(startPos, searchDir)
    if(claimedPipes[startPos[0]][startPos[1]] or startPos in cyclePipes): return claimedPipes

    pipesToCheck = [startPos]
    while(len(pipesToCheck) > 0):
        currPipe = pipesToCheck.pop(0)
        if(currPipe not in cyclePipes and not claimedPipes[currPipe[0]][currPipe[1]] and
           currPipe[0] > 0 and currPipe[0] < len(claimedPipes) - 1 and
           currPipe[1] > 0 and currPipe[1] < len(claimedPipes[0]) - 1):
            claimedPipes[currPipe[0]][currPipe[1]] = True
            pipesToCheck.append(move(currPipe, direction.UP))
            pipesToCheck.append(move(currPipe, direction.DOWN))
            pipesToCheck.append(move(currPipe, direction.LEFT))
            pipesToCheck.append(move(currPipe, direction.RIGHT))
    
    return claimedPipes



def part2(filename):
    pipes = getInput(filename).splitlines()

    #find start location
    sLoc = None
    for i, row in enumerate(pipes):
        for j, char in enumerate(row):
            if(char == "S"):
                sLoc = (i, j)
    if(sLoc == None): return -1

    #find adjacent tile to start search from
    searchDirection = direction.NONE
    if(sLoc[0] > 0): #search up
        pipe = pipes[sLoc[0] - 1][sLoc[1]]
        if (pipe in "|F7"):
            searchDirection = direction.UP
    if(searchDirection == direction.NONE and sLoc[0] < len(pipes) - 1): #search down
        pipe = pipes[sLoc[0] + 1][sLoc[1]]
        if (pipe in "|JL"):
            searchDirection = direction.DOWN
    if(searchDirection == direction.NONE and sLoc[1] > 0): #search left
        pipe = pipes[sLoc[0]][sLoc[1] - 1]
        if (pipe in "-FL"):
            searchDirection = direction.LEFT
    if(searchDirection == direction.NONE and sLoc[1] < len(pipes[0]) - 1): #search right
        pipe = pipes[sLoc[0]][sLoc[1] + 1]
        if (pipe in "-J7"):
            searchDirection = direction.RIGHT
    
    if(searchDirection == direction.NONE): return -2

    #check whether loop is "right" loop or "left" loop
    pipePositions = [sLoc]
    currPos = move(sLoc, searchDirection)
    currDirection = searchDirection
    lefts, rights = 0, 0
    while(pipes[currPos[0]][currPos[1]] != "S"):
        pipePositions.append(currPos)

        pipe = pipes[currPos[0]][currPos[1]]
        currDirection, wentLeft = rotateAndIsLeft(pipe, currDirection)
        currPos = move(currPos, currDirection)

        if(wentLeft): lefts += 1
        elif(wentLeft != None): rights += 1
    
    
    totalClockwise = rights - lefts
    loopDir = None # -1 == left, 1 == right
    if(totalClockwise > 0): #should be 4 or -4, +/- 1 due to start pipe not accounted for
        loopDir = 1
    elif(totalClockwise < 0):
        loopDir = -1
    else:
        return -3

    #figure out which pipes are contained in the pipe
    containedPipes = [[False for y in x] for x in pipes]
    currPos = move(sLoc, searchDirection)
    currDirection = searchDirection
    while(pipes[currPos[0]][currPos[1]] != "S"):
        pipe = pipes[currPos[0]][currPos[1]]
        currDirection = rotate(pipe, currDirection)
        containedPipes = claimPipes(containedPipes, pipePositions, currPos, rotateDir(currDirection, loopDir == -1))
        currPos = move(currPos, currDirection)
        containedPipes = claimPipes(containedPipes, pipePositions, currPos, rotateDir(currDirection, loopDir == -1))


    return sum([sum([1 for y in x if y]) for x in containedPipes])





def main():
    print("part 1:", part1("input.txt"))
    print("part 2:", part2("input.txt"))

if(__name__ == "__main__"):
    main()