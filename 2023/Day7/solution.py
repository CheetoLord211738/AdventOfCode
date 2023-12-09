
import functools

def getInput(filename):
    with open(filename, "r") as f:
        data = f.read()
        return data



def countOccurances(cards, card):
    return len(['1' for x in cards if x == card])

def countUniqueCards(cards):
    unique = 0
    while (len(cards) > 0):
        cards = cards.replace(cards[0], '')
        unique += 1
    return unique

def fiveOfAKind(cards):
    return countUniqueCards(cards) == 1

def fourOfAKind(cards):
    if (countUniqueCards(cards) != 2): return False
    return countOccurances(cards, cards[0]) == 4 or countOccurances(cards, cards[0]) == 1

# assumes fourOfAKind returned false
def fullHouse(cards):
    return countUniqueCards(cards) == 2

def threeOfAKind(cards):
    if (countUniqueCards(cards) != 3): return False
    return (countOccurances(cards, cards[0]) == 3 or
            countOccurances(cards, cards[1]) == 3 or
            countOccurances(cards, cards[2]) == 3)

# assumes threeOfAKind returned false
def twoPair(cards):
    return countUniqueCards(cards) == 3

def onePair(cards):
    return countUniqueCards(cards) == 4

def calcType(cards):
    if(fiveOfAKind(cards)): return 7
    if(fourOfAKind(cards)): return 6
    if(fullHouse(cards)): return 5
    if(threeOfAKind(cards)): return 4
    if(twoPair(cards)): return 3
    if(onePair(cards)): return 2
    # high card
    return 1



def getCardScore(card):
    return "23456789TJQKA".index(card)

def compare(hand1, hand2):
    hand1 = hand1[:5]
    hand2 = hand2[:5]
    hand1Type = calcType(hand1)
    hand2Type = calcType(hand2)

    if(hand1 == hand2): return 0

    #first sort by hand type
    if(hand1Type > hand2Type):
        return 1
    elif(hand1Type < hand2Type):
        return -1
    
    #tie breaker
    for i in range(len(hand1)):
        card1 = hand1[i]
        card2 = hand2[i]
        score1 = getCardScore(card1)
        score2 = getCardScore(card2)
        if(score1 > score2):
            return 1
        elif(score1 < score2):
            return -1
    
    # ?
    return 0


def compare(hand1, hand2):
    hand1 = hand1[:5]
    hand2 = hand2[:5]
    hand1Type = calcType(hand1)
    hand2Type = calcType(hand2)

    if(hand1 == hand2): return 0

    #first sort by hand type
    if(hand1Type > hand2Type):
        return 1
    elif(hand1Type < hand2Type):
        return -1
    
    #tie breaker
    for i in range(len(hand1)):
        card1 = hand1[i]
        card2 = hand2[i]
        score1 = getCardScore(card1)
        score2 = getCardScore(card2)
        if(score1 > score2):
            return 1
        elif(score1 < score2):
            return -1
    
    # ?
    return 0



def part1(filename):
    hands = getInput(filename).splitlines()
    hands = sorted(hands, key=functools.cmp_to_key(compare))

    total = 0
    for rank, hand in enumerate(hands):
        bid = int(hand[6:])
        total += bid * (rank+1)

    return total




# nearly identical getCardScore function, but considers J to be the weakest
def getCardScore2(card):
    return "J23456789TQKA".index(card)

# nearly identical compare function, but with tiebreakers considering J to be the weakest,
# and turning J's into what is best for the hand before type comparison
def compare2(hand1, hand2):
    hand1 = hand1[:5]
    hand2 = hand2[:5]
    hand1Type = calcType(bestHand(hand1))
    hand2Type = calcType(bestHand(hand2))

    if(hand1 == hand2): return 0

    #first sort by hand type
    if(hand1Type > hand2Type):
        return 1
    elif(hand1Type < hand2Type):
        return -1
    
    #tie breaker
    for i in range(len(hand1)):
        card1 = hand1[i]
        card2 = hand2[i]
        score1 = getCardScore2(card1)
        score2 = getCardScore2(card2)
        if(score1 > score2):
            return 1
        elif(score1 < score2):
            return -1
    
    # ?
    return 0



def bestHand(hand):
    if("J" not in hand): return hand
    if(hand == "JJJJJ"): return "AAAAA" #handling edge case

    # turning all J's into the most common currently existing card
    # in the hand is always best for this ruleset. No brute forcing needed :)

    # This is ineeficient, but whatever, its only 5 characters, and I can't think of anything better.
    mostFrequentCard = ''
    occurances = 0
    for card in hand:
        if(card == "J"): continue
        cardCount = countOccurances(hand, card)
        if(cardCount > occurances):
            occurances = cardCount
            mostFrequentCard = card
    
    return hand.replace("J", mostFrequentCard)


def part2(filename):
    hands = getInput(filename).splitlines()
    hands = sorted(hands, key=functools.cmp_to_key(compare2))

    total = 0
    for rank, hand in enumerate(hands):
        bid = int(hand[6:])
        total += bid * (rank+1)

    return total




def main():
    print("part 1:", part1("input.txt"))
    print("part 2:", part2("input.txt"))

if(__name__ == "__main__"):
    main()