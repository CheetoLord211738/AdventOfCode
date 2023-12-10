
import math

def getInput(filename):
    with open(filename, "r") as f:
        data = f.read()
        return data


def constructDicts(nodes):
    lefts = {}
    rights = {}
    for node in nodes:
        name = node[:3]
        lefts[name] = node[7:10]
        rights[name] = node[12:15]
    return (lefts, rights)

def part1(filename):
    data = getInput(filename)
    path = data.splitlines()[0]
    (lefts, rights) = constructDicts(data.splitlines()[2:])

    currNode = "AAA"
    pathIndex = 0
    steps = 0
    while (currNode != "ZZZ"):
        nextStep = path[pathIndex]
        pathIndex += 1
        if(pathIndex >= len(path)):
            pathIndex = 0
        
        if(nextStep == "L"):
            currNode = lefts[currNode]
        else:
            currNode = rights[currNode]
        steps += 1

    return steps






def findLength(startNode, lefts, rights, path):
    currNode = startNode
    pathIndex = 0
    steps = 0
    while (currNode[2] != "Z"):
        nextStep = path[pathIndex]
        pathIndex += 1
        if(pathIndex >= len(path)):
            pathIndex = 0
        
        if(nextStep == "L"):
            currNode = lefts[currNode]
        else:
            currNode = rights[currNode]
        steps += 1
    return steps




def part2(filename):
    data = getInput(filename)
    path = data.splitlines()[0]
    nodes = data.splitlines()[2:]
    (lefts, rights) = constructDicts(nodes)

    currNodes = []
    for node in nodes:
        name = node[:3]
        if(name[2] == "A"):
            currNodes.append(name)

    lengths = []
    for node in currNodes:
        lengths.append(findLength(node, lefts, rights, path))
    
    
    totalLCD = 1
    for length in lengths:
        totalLCD = math.lcm(totalLCD, length)

    
    return totalLCD




def main():
    print("part 1:", part1("input.txt"))
    print("part 2:", part2("input.txt"))

if(__name__ == "__main__"):
    main()