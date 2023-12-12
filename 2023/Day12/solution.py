
def getInput(filename):
    with open(filename, "r") as f:
        data = f.read()
        return data




knownPositions = {}

def possibleCombos(springs, sequences):
    if(len(sequences) == 0) : return (1 if "#" not in springs else 0)

    myPos = springs + ','.join([str(x) for x in sequences])
    if(myPos in knownPositions): return knownPositions[myPos]

    currSequence = sequences[0]
    furthestSpace = len(springs) - (sum(sequences) + len(sequences) - 1)
    #print(furthestSpace)
    possibilities = 0
    for i in range(furthestSpace+1):
        if ("." in springs[i:i + currSequence]): continue
        if(i + currSequence < len(springs)):
            if (springs[i + currSequence] == "#"): continue
        if ("#" in springs[:i]): break
        #print(i, len(sequences))
        possibilities += possibleCombos(springs[i + currSequence + 1:], sequences[1:])

    knownPositions[myPos] = possibilities
    return possibilities


def part1(filename):
    rows = getInput(filename).splitlines()

    total = 0
    for row in rows:
        springs = row.split(" ")[0]
        sequences = [int(x) for x in row.split(" ")[1].split(",")]
        possibilities = possibleCombos(springs, sequences)
        total += possibilities

    return total







def part2(filename):
    rows = getInput(filename).splitlines()

    total = 0
    for i, row in enumerate(rows):
        springs = "?".join([row.split(" ")[0] for _ in range(5)])
        sequences = [int(x) for x in ",".join([row.split(" ")[1] for _ in range(5)]).split(",")]
        possibilities = possibleCombos(springs, sequences)
        total += possibilities

    return total





def main():
    print("part 1:", part1("input.txt"))
    print("part 2:", part2("input.txt"))

if(__name__ == "__main__"):
    main()