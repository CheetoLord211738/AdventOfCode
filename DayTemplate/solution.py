
def getInput(filename):
    with open(filename, "r") as f:
        data = f.read()
        return data



def part1(filename):
    data = getInput(filename)
    return 0




def part2(filename):
    data = getInput(filename)
    return 0



def main():
    print("part 1:", part1("input.txt"))
    print("part 2:", part2("input.txt"))

if(__name__ == "__main__"):
    main()