
import re

def getInput(filename):
    with open(filename, "r") as f:
        data = f.read()
        return data


def isPossible(game, reds, greens, blues):
    sets = re.match("^Game \d+: (.*)", game).group(1).split("; ")

    for set in sets:
        redCount = re.match(".*?(\d+) red", set)
        redCount = 0 if (redCount == None) else int(redCount.group(1))
        
        greenCount = re.match(".*?(\d+) green", set)
        greenCount = 0 if (greenCount == None) else int(greenCount.group(1))
        
        blueCount = re.match(".*?(\d+) blue", set)
        blueCount = 0 if (blueCount == None) else int(blueCount.group(1))

        if(redCount > reds or greenCount > greens or blueCount > blues):
            return False
    
    return True

def part1(filename):
    reds = 12
    greens = 13
    blues = 14

    games = getInput(filename).splitlines()

    total = 0
    for game in games:
        gameID = int(re.match("^Game (\d+)", game).group(1))
        if(isPossible(game, reds, greens, blues)):
            total += gameID
    
    return total




def calcPower(game):
    reds = re.findall(".*?(\d+) red", game)
    maxReds = max([int(find) for find in reds])

    greens = re.findall(".*?(\d+) green", game)
    maxGreens = max([int(find) for find in greens])

    blues = re.findall(".*?(\d+) blue", game)
    maxBlues = max([int(find) for find in blues])

    return maxReds*maxGreens*maxBlues


def part2(filename):
    games = getInput(filename).splitlines()

    total = 0
    for game in games:
        total += calcPower(game)
    
    return total




def main():
    print("part 1:", part1("input.txt"))
    print("part 2:", part2("input.txt"))


if (__name__ == "__main__"):
    main()