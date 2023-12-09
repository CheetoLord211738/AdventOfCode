
def getInput(filename):
    with open(filename, "r") as f:
        data = f.read()
        return data
    





def getValue(row, col, list):
    if(row < 0 or col < 0): return False
    if(row >= len(list) or col >= len(list[0])): return False
    return list[row][col]

def hasAdjacentSymbol(row, col, list):
    if (getValue(row-1, col-1, list)): return True
    if (getValue(row-1, col, list)): return True
    if (getValue(row-1, col+1, list)): return True
    if (getValue(row, col-1, list)): return True
    if (getValue(row, col+1, list)): return True
    if (getValue(row+1, col-1, list)): return True
    if (getValue(row+1, col, list)): return True
    if (getValue(row+1, col+1, list)): return True

    return False

def printBool2DArray(data):
    for line in data:
        for value in line:
            print("#" if value else ".", end="")
        print()

def part1(filename):
    data = getInput(filename).splitlines()
    symbolList = [[False for character in line] for line in data]
    numberList = [row.copy() for row in symbolList]

    # mark all symbols
    for i, line in enumerate(data):
        for j, character in enumerate(line):
            if(character != "." and not character.isdigit()):
                symbolList[i][j] = True

    # mark all immediately adjacent numbers
    for i, line in enumerate(data):
        for j, character in enumerate(line):
            if(hasAdjacentSymbol(i, j, symbolList) and character.isdigit()):
                numberList[i][j] = True

    # mark digits immediately left and right of symbl-adjacent digits
    for i, line in enumerate(data):
        for j, character in enumerate(line):
            if(numberList[i][j]):
                # expand number left
                currCol = j - 1
                while(currCol >= 0 and data[i][currCol].isdigit()):
                    numberList[i][currCol] = True
                    currCol -= 1
                
                # expand number right
                currCol = j + 1
                while(currCol < len(line) and data[i][currCol].isdigit()):
                    numberList[i][currCol] = True
                    currCol += 1

    #find all numbers based on numberList
    numbers = []
    for i, line in enumerate(numberList):
        currNumber = ""
        for j, isValid in enumerate(line):
            if(isValid):
                currNumber += data[i][j]
            elif (currNumber != ""):
                numbers.append(int(currNumber))
                currNumber = ""
        if (currNumber != ""):
                numbers.append(int(currNumber))

    return sum(numbers)










def getCharacter(row, col, list):
    if(row < 0 or col < 0): return "."
    if(row >= len(list) or col >= len(list[0])): return "."
    return list[row][col]

def getAdjacentDigits(row, col, list):
    digitPosList = []
    if (getCharacter(row-1, col-1, list).isdigit()): digitPosList.append((row-1, col-1))
    if (getCharacter(row-1, col, list).isdigit()): digitPosList.append((row-1, col))
    if (getCharacter(row-1, col+1, list).isdigit()): digitPosList.append((row-1, col+1))
    if (getCharacter(row, col-1, list).isdigit()): digitPosList.append((row, col-1))
    if (getCharacter(row, col+1, list).isdigit()): digitPosList.append((row, col+1))
    if (getCharacter(row+1, col-1, list).isdigit()): digitPosList.append((row+1, col-1))
    if (getCharacter(row+1, col, list).isdigit()): digitPosList.append((row+1, col))
    if (getCharacter(row+1, col+1, list).isdigit()): digitPosList.append((row+1, col+1))
    return digitPosList


def expandNumber(row, col, list):
    num = list[row][col]
    # expand number left
    currCol = col - 1
    while(currCol >= 0 and list[row][currCol].isdigit()):
        num = list[row][currCol] + num
        currCol -= 1
                
    # expand number right
    currCol = col + 1
    while(currCol < len(list[0]) and list[row][currCol].isdigit()):
        num += list[row][currCol]
        currCol += 1

    return int(num)


def part2(filename):
    data = getInput(filename).splitlines()
    gearList = []

    # find all gears
    for i, line in enumerate(data):
        for j, character in enumerate(line):
            if(character == "*"):
                gearList.append((i, j))

    total = 0
    # find adjacent numbers for each gear and calculate "gear ratios" (also weeds out asterisks with only one adjacent number)
    for gear in gearList:
        row = gear[0]
        col = gear[1]
        adjDigits = getAdjacentDigits(row, col, data)

        # set used to prevent duplicate numbers when multiple digits of that number are adjacent to the gear.
        # kind of banks on no gears having 2 identical numbers next to it, but oh well.
        allNums = set()
        for digit in adjDigits:
            digitRow = digit[0]
            digitCol = digit[1]
            allNums.add(expandNumber(digitRow, digitCol, data))
        
        if (len(allNums) < 2):
            # not a gear
            continue

        elif (len(allNums) > 2):
            # Ive got a bug
            raise Exception("Too many IDs for gear (pos = {row}, {col})")

        # its a product, not a ratio. Gotta be consistent with the naming though, i suppose...
        gearRatio = allNums.pop()*allNums.pop()
        total += gearRatio

    return total


def main():
    print("part 1:", part1("input.txt"))
    print("part 2:", part2("input.txt"))

if(__name__ == "__main__"):
    main()