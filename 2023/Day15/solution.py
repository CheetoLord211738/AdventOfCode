
def getInput(filename):
    with open(filename, "r") as f:
        data = f.read()
        return data



def HASH(string):
    hash = 0
    for char in string:
        hash += ord(char)
        hash *= 17
        hash %= 256
    return hash


def part1(filename):
    data = getInput(filename).split(",")
    total = 0
    for string in data:
        total += HASH(string)
    return total

    



def addLens(label, focalLength):
    targetBox = HASH(label)
    if(label in [x[0] for x in boxes[targetBox]]):
        labelPos = [x[0] for x in boxes[targetBox]].index(label)
        boxes[targetBox][labelPos] = (label, focalLength)
    else:
        boxes[targetBox].append((label, focalLength))


def removeLens(label):
    targetBox = HASH(label)
    if(label in [x[0] for x in boxes[targetBox]]):
        labelPos = [x[0] for x in boxes[targetBox]].index(label)
        boxes[targetBox].pop(labelPos)



boxes = {x: [] for x in range(256)}
def part2(filename):
    HASHMAP = getInput(filename).split(",")
    for instr in HASHMAP:
        if("=" in instr):
            label = instr.split("=")[0]
            focalLength = int(instr.split("=")[1])
            addLens(label, focalLength)
        else:
            label = instr.split("-")[0]
            removeLens(label)

    focusingPowerTotal = 0
    for box in range(256):
        currBox = boxes[box]
        for pos, lens in enumerate(currBox):
            focusingPower = (box+1) * (lens[1]) * (pos+1)
            focusingPowerTotal += focusingPower
    
    return focusingPowerTotal



def main():
    print("part 1:", part1("input.txt"))
    print("part 2:", part2("input.txt"))

if(__name__ == "__main__"):
    main()