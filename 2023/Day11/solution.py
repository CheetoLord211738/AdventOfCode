
def getInput(filename):
    with open(filename, "r") as f:
        data = f.read()
        return data



def part1(filename):
    universe = getInput(filename).splitlines()

    #extend vertically
    i = 0
    while (i < len(universe)):
        line = universe[i]
        if(len([char for char in line if char == "#"]) == 0):
            universe.insert(i, line)
            i += 1
        i += 1
    
    #extend horixzontally
    i = 0
    while (i < len(universe[0])):
        column = ''.join([universe[x][i] for x in range(len(universe))])
        if(len([char for char in column if char == "#"]) == 0):
            universe = [x[:i] + "." + x[i:] for x in universe]
            i += 1
        i += 1
    

    #find all galaxies
    galaxies = []
    for i, row in enumerate(universe):
        for j, char in enumerate(row):
            if (char == "#"):
                galaxies.append((i, j))
    
    # sum all distances
    total = 0
    for i, galaxy1 in enumerate(galaxies):
        for galaxy2 in galaxies[i+1:]:
            total += abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])

    return total




def calcRealPos(y, x, vExtentions, hExtentions):
    realX = x + (999_999 * len([i for i in hExtentions if i < x]))
    realY = y + (999_999 * len([i for i in vExtentions if i < y]))
    return (realY, realX)



def part2(filename):
    universe = getInput(filename).splitlines()

    #mark vertical extensions
    verticalExtentionIndecies = []
    for i, line in enumerate(universe):
        if(len([char for char in line if char == "#"]) == 0):
            verticalExtentionIndecies.append(i)
    
    #mark horizontal extensions
    horizontalExtentionIndecies = []
    for i in range(len(universe[0])):
        column = ''.join([universe[x][i] for x in range(len(universe))])
        if(len([char for char in column if char == "#"]) == 0):
            horizontalExtentionIndecies.append(i)

    #find all galaxies
    galaxies = []
    for i, row in enumerate(universe):
        for j, char in enumerate(row):
            if (char == "#"):
                realPos = calcRealPos(i, j, verticalExtentionIndecies, horizontalExtentionIndecies)
                galaxies.append(realPos)
    
    # sum all distances
    total = 0
    for i, galaxy1 in enumerate(galaxies):
        for galaxy2 in galaxies[i+1:]:
            total += abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])

    return total




def main():
    print("part 1:", part1("input.txt"))
    print("part 2:", part2("input.txt"))

if(__name__ == "__main__"):
    main()