
def getInput(filename):
    with open(filename, "r") as f:
        data = f.read()
        return data



def extrapolateNext(values):
    # base case, all zeroes
    if(len([x for x in values if x != 0]) == 0): return 0

    newValues = []
    for i in range(len(values) - 1):
        newValues.append(values[i + 1] - values[i])

    return values[-1] + extrapolateNext(newValues)


def part1(filename):
    histories = getInput(filename).splitlines()

    total = 0
    for history in histories:
        values = [int(x) for x in history.split(" ")]
        total += extrapolateNext(values)

    return total





def extrapolateBack(values):
    # base case, all zeroes
    if(len([x for x in values if x != 0]) == 0): return 0

    newValues = []
    for i in range(len(values) - 1):
        newValues.append(values[i + 1] - values[i])

    return values[0] - extrapolateBack(newValues)


def part2(filename):
    histories = getInput(filename).splitlines()

    total = 0
    for history in histories:
        values = [int(x) for x in history.split(" ")]
        total += extrapolateBack(values)

    return total




def main():
    print("part 1:", part1("input.txt"))
    print("part 2:", part2("input.txt"))

if(__name__ == "__main__"):
    main()