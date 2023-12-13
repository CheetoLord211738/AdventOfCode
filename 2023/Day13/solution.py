
def getInput(filename):
    with open(filename, "r") as f:
        data = f.read()
        return data



def isMirror(pattern, index):
    index1 = index - 1
    index2 = index
    while(index1 >= 0 and index2 < len(pattern)):
        if(pattern[index1] != pattern[index2]): return False
        index1 -= 1
        index2 += 1
    return True



def findMirror(pattern):
    for i in range(1, len(pattern)):
        if(isMirror(pattern, i)): return i
    return -1




def findSplit(pattern):
    vPattern = [[pattern[y][z] for y in range(len(pattern))] for z in range(len(pattern[0]))]
    vSplit = findMirror(vPattern)
    if(vSplit > -1): return vSplit

    hPattern = [x.replace("#", "1").replace(".", "0") for x in pattern]
    return findMirror(hPattern) * 100



def part1(filename):
    patterns = getInput(filename).split("\n\n")

    total = 0
    for pattern in patterns:
        total += findSplit(pattern.splitlines())

    return total






def countDifferences(pattern1, pattern2):
    return len([1 for x in range(len(pattern1)) if pattern1[x] != pattern2[x]])



def isSmudgedMirror(pattern, index):
    index1 = index - 1
    index2 = index
    differences = 0
    while(index1 >= 0 and index2 < len(pattern) and differences < 2):
        differences += countDifferences(pattern[index1], pattern[index2])
        index1 -= 1
        index2 += 1
    return differences == 1




def findSmudgedMirror(pattern):
    for i in range(1, len(pattern)):
        if(isSmudgedMirror(pattern, i)): return i
    return -1




def findSmudgedSplit(pattern):
    vPattern = [[pattern[y][z] for y in range(len(pattern))] for z in range(len(pattern[0]))]
    vSplit = findSmudgedMirror(vPattern)
    if(vSplit > -1): return vSplit

    hPattern = [x.replace("#", "1").replace(".", "0") for x in pattern]
    return findSmudgedMirror(hPattern) * 100





def part2(filename):
    patterns = getInput(filename).split("\n\n")

    total = 0
    for pattern in patterns:
        total += findSmudgedSplit(pattern.splitlines())

    return total




def main():
    print("part 1:", part1("input.txt"))
    print("part 2:", part2("input.txt"))

if(__name__ == "__main__"):
    main()