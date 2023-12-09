
import re

def getInput(filename):
    with open(filename, "r") as f:
        data = f.read()
        return data


def calcDistance(holdTime, totalTime):
    return holdTime * (totalTime - holdTime)


def calcMargin(time, record):
    totalWins = 0
    for i in range(time):
        if(calcDistance(i, time) > record):
            totalWins += 1
    return totalWins


def part1(filename):
    data = getInput(filename).splitlines()
    times = [int(x) for x in re.sub(" +", " ", data[0]).split(" ")[1:]]
    records = [int(x) for x in re.sub(" +", " ", data[1]).split(" ")[1:]]
    
    product = 1
    for i in range(len(times)):
        product *= calcMargin(times[i], records[i])

    return product





def part2(filename):
    data = getInput(filename).splitlines()
    time = int(''.join([x for x in data[0] if x.isdigit()]))
    record = int(''.join([x for x in data[1] if x.isdigit()]))
    
    return calcMargin(time, record)







def main():
    print("part 1:", part1("input.txt"))
    print("part 2:", part2("input.txt"))

if(__name__ == "__main__"):
    main()