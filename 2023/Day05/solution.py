
import functools

def getInput(filename):
    with open(filename, "r") as f:
        data = f.read()
        return data



def convertValue(value, conversion):
    conversion = conversion.split("\n")[1:]
    for rangeMap in conversion:
        rangeMap = rangeMap.split(" ")
        dest = int(rangeMap[0])
        source = int(rangeMap[1])
        length = int(rangeMap[2])

        if (value >= source and value < source + length):
            return value + (dest - source)
    
    return value

def part1(filename):
    alminac = getInput(filename).split("\n\n")
    currentValues = [int(x) for x in alminac[0].split(" ")[1:]]
    alminac = alminac[1:]

    for conversion in alminac:
        newValues = []
        for value in currentValues:
            newValues.append(convertValue(value, conversion))
        currentValues = newValues

    return min(currentValues)





# any time an "end" of a range is referenced here, it denotes the first value past the range (so it is NOT in the range)
def convertRange(myRange, conversion):
    # sort ranges based on start of source range
    conversion = sorted(conversion.split("\n")[1:], key=functools.cmp_to_key(lambda x, y: -1 if (int(x.split(" ")[1]) <= int(y.split(" ")[1])) else (0 if (int(x.split(" ")[1]) == int(y.split(" ")[1])) else 1)))

    # print(f"Making new range from {myRange}...")
    myRangeStart = myRange[0]
    myRangeLength = myRange[1]
    
    newRanges = []
    for rangeMap in conversion:
        rangeMap = rangeMap.split(" ")
        dest = int(rangeMap[0])
        source = int(rangeMap[1])
        length = int(rangeMap[2])

        # myRange is past this range, skip it
        if(myRangeStart >= source + length):
            # print(f"Not in ({source}, {length})...")
            continue

        # manage excess values before next range
        if(myRangeStart < source):
            # print("Adding excess...")
            # make a new range with same values as myRange up until conversion data starts
            newRangeStart = myRangeStart
            newRangeLength = min(myRangeLength, source - myRangeStart)
            newRanges.append((newRangeStart, newRangeLength))
            
            # move myRange variables to mark what is left
            myRangeStart = myRangeStart + newRangeLength
            myRangeLength -= newRangeLength
        
        # make new range with conversion data
        if(myRangeStart >= source):
            # print(f"Converting using ({dest}, {source}, {length})")
            # make a new range with shifted values up until conversion data ends or myRange ends
            newRangeStart = max(myRangeStart, source)
            newRangeLength = min(myRangeLength, length - (newRangeStart - source))
            newRangeStart += dest - source     # adjust for dest
            newRanges.append((newRangeStart, newRangeLength))

            # move myRange variables to mark what is left
            myRangeStart = myRangeStart + newRangeLength
            myRangeLength -= newRangeLength

        # if exhausted myRange
        if(myRangeLength == 0):
            break

    # handle all of myRange that lies past all conversion ranges
    if(myRangeLength > 0):
        # print("adding end excess...")
        newRanges.append((myRangeStart, myRangeLength))

    # print(f"Range is now {newRanges}\n")
    return newRanges



def rangeInRange(range1, range2):
    range1Start = range1[0]
    range1Length = range1[1]
    range1End = range1Start + range1Length

    range2Start = range2[0]
    range2Length = range2[1]
    range2End = range2Start + range2Length

    return range1Start >= range2Start and range1End <= range2End


# this function won't be called if one range is fully in aonother, so we ignore this case
def rangeOverlaps(range1, range2):
    range1Start = range1[0]
    range1Length = range1[1]
    range1End = range1Start + range1Length

    range2Start = range2[0]
    range2Length = range2[1]
    range2End = range2Start + range2Length

    R1thenR2 = range1End <= range2End and range1End >= range2Start
    R2thenR1 = range2End <= range1End and range2End >= range1Start

    return R1thenR2 or R2thenR1


def combineRanges(range1, range2):
    range1Start = range1[0]
    range1Length = range1[1]
    range1End = range1Start + range1Length

    range2Start = range2[0]
    range2Length = range2[1]
    range2End = range2Start + range2Length

    newRangeStart = min(range1Start, range2Start)
    newRangeEnd = max(range1End, range2End)
    newRangeLength = newRangeEnd - newRangeStart

    return (newRangeStart, newRangeLength)



def condenseRanges(ranges):
    # print("Condensing", ranges)
    comparePos1 = 0
    while(comparePos1 < len(ranges) - 1):
        targetRange1 = ranges[comparePos1]

        comparePos2 = comparePos1 + 1
        while(comparePos2 < len(ranges)):
            targetRange2 = ranges[comparePos2]
            
            # check if targetRange1 is completely in taretRange2
            if(rangeInRange(targetRange1, targetRange2)):
                # targetRange1 is redundant
                ranges.pop(comparePos1)
                # print("TargetRange1 {targetRange1} is reduntant")
                
                # update which range is being checked
                targetRange1 = ranges[comparePos1]
                comparePos2 -= 1    # deleted an earlier element, so move the serach back an index
            
            # check if targetRange2 is completely in taretRange1
            elif(rangeInRange(targetRange2, targetRange1)):
                # targetRange2 is redundant
                ranges.pop(comparePos2)
                # print("TargetRange2 {targetRange2} is reduntant")
                
                # deleted an element, so move the serach back an index
                comparePos2 -= 1

            # check if the ranges overlap
            elif(rangeOverlaps(targetRange1, targetRange2)):
                #remove ranges, we will be combining them
                ranges.pop(comparePos2)
                ranges.pop(comparePos1)

                newRange = combineRanges(targetRange1, targetRange2)
                ranges.append(newRange)

                # print("{targetRange1} and {targetRange2} are now {newRange}")

                # we got rid of comparePos1's element, move on to the next one
                # but first, shift comparePos1 back, as an element was removed
                # (comparePos2 will be overwritten anyways, no need to update)
                comparePos1 -= 1
                break # break out of inner while loop


            comparePos2 += 1

        comparePos1 += 1

    # print("Done! ranges are now", ranges, "\n")
    return ranges




def part2(filename):
    alminac = getInput(filename).split("\n\n")
    seedValues = [int(x) for x in alminac[0].split(" ")[1:]]
    alminac = alminac[1:]

    currentRanges = []
    for i in range(0, len(seedValues), 2):
        currentRanges.append((seedValues[i], seedValues[i+1]))

    for conversion in alminac:
        newRanges = []
        for seedRange in currentRanges:
            newRanges += convertRange(seedRange, conversion)
        # print("New ranges are now", newRanges)
        # this condensation may be entirely redundant, but I added it just in case overlapping ranges are frequent and exponentiate
        currentRanges = condenseRanges(newRanges)
    
    return min([x[0] for x in currentRanges])








def main():
    print("part 1:", part1("input.txt"))
    print("part 2:", part2("input.txt"))

if(__name__ == "__main__"):
    main()