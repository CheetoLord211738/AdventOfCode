
import re

def getInput(filename):
    with open(filename, "r") as f:
        data = f.read()
        return data

def part1(filename):
    data = getInput(filename).splitlines()
    nums = []
    for line in data:
        firstDigit = int(re.search("^.*?(\d)", line).group(1))
        lastDigit = int(re.search("(\d)[^\d]*$", line).group(1))
        num = firstDigit*10 + lastDigit
        nums.append(num)
    return sum(nums)



def strToNum(myStr):
    if re.search("\d", myStr) != None: #if is a digit
        return int(myStr)
    else: #is a word ("one", "two", etc)
        return ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"].index(myStr)

def part2(filename):
    data = getInput(filename).splitlines()
    nums = []
    for line in data:
        firstDigit = strToNum(re.search("^.*?(\d|one|two|three|four|five|six|seven|eight|nine)", line).group(1))
        lastDigit = strToNum(re.search(".*(\d|one|two|three|four|five|six|seven|eight|nine).*?$", line).group(1))
        num = firstDigit*10 + lastDigit
        nums.append(num)
    return sum(nums)




def main():
    print("part 1:", part1("input.txt"))
    print("part 2:", part2("input.txt"))

if(__name__ == "__main__"):
    main()