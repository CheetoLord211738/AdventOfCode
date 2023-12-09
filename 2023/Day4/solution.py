
import re

def getInput(filename):
    with open(filename, "r") as f:
        data = f.read()
        return data



def scoreCard(card):
    card = card[10:]

    winningNumbers = []
    while (card[0] != "|"):
        winningNumbers.append(int(card[:3]))
        card = card[3:]

    card = card[1:]

    myNumbers = []
    while (len(card) > 0):
        myNumbers.append(int(card[:3]))
        card = card[3:]

    score = 0
    for num in myNumbers:
        if (num in winningNumbers):
            score = max(1, score*2)

    return score


def part1(filename):
    cards = getInput(filename).splitlines()

    total = 0
    for card in cards:
        total += scoreCard(card)

    return total







def scoreCardLinear(card):
    card = card[10:]

    winningNumbers = []
    while (card[0] != "|"):
        winningNumbers.append(int(card[:3]))
        card = card[3:]

    card = card[1:]

    myNumbers = []
    while (len(card) > 0):
        myNumbers.append(int(card[:3]))
        card = card[3:]

    score = 0
    for num in myNumbers:
        if (num in winningNumbers):
            score += 1

    return score


def part2(filename):
    cards = getInput(filename).splitlines()
    scratchcardCounts = [1 for _ in cards]

    for i, card in enumerate(cards):
        score = scoreCardLinear(card)
        numCards = scratchcardCounts[i]

        for j in range(1, score+1):
            scratchcardCounts[i+j] += numCards

    return sum(scratchcardCounts)




def main():
    print("part 1:", part1("input.txt"))
    print("part 2:", part2("input.txt"))

if(__name__ == "__main__"):
    main()