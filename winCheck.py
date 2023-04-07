import copy
import logging
import logging.handlers

import logging
logger = logging.getLogger(__name__)


kicker = 0
scoreList = [[],[],[],[]]

def flushCheck(card1, card2, tableList, playerNum):
    tableCards = copy.deepcopy(tableList)
    colorList = [[],[],[],[]]
    tableCards.append(card1)
    tableCards.append(card2)
    sorted(tableCards)
    logger.debug(f'flushDeck tableCards: {tableCards}')
    for i in range(len(tableCards)):
        if tableCards[i][0] == 'C':
            colorList[0].append('Club')
        elif tableCards[i][0] == 'D':
            colorList[1].append('Diamond')
        elif tableCards[i][0] == 'S':
            colorList[2].append('Spade')
        else:
            colorList[3].append('Heart')

    if len(colorList[0]) >= 5 or len(colorList[1]) >= 5 or len(colorList[2]) >= 5 or len(colorList[3]) >= 5:
        logger.debug("This is probably a flush")
        logger.debug(len(colorList[0]))
        logger.debug(len(colorList[1]))
        logger.debug(colorList)
        return True
    else:
        logger.debug("This probably isn't a flush")
        logger.debug(len(colorList[0]))
        logger.debug(len(colorList[1]))
        logger.debug(colorList)

def pairCheck(card1, card2, tableList, playerNum):
    global kicker
    tableCards = copy.deepcopy(tableList)
    pairCount = 0
    numList = []
    pairList = []
    tableCards.append(card1)
    tableCards.append(card2)
    sorted(tableCards)
    logger.debug(f'pairCheck tableCards: {tableCards}')
    for i in range(len(tableCards)):
        if tableCards[i][1] == '0':
            numList.append(10)
        elif tableCards[i][1] == 'J':
            numList.append(11)
        elif tableCards[i][1] == 'Q':
            numList.append(12)
        elif tableCards[i][1] == 'K':
            numList.append(13)
        elif tableCards[i][1] == 'A':
            numList.append(14)
        else:
            numList.append(int(tableCards[i][1]))
    numList.sort()
    for x in range(len(numList)):
        logger.debug(f'**paircheck key value "x": {x} and the card num in question is: {numList[x]} and the tableCards[x] value is: {tableCards[x]}')
        z = 1
        for y in range(len(numList)):
            if numList[x] == numList[y]:
                if z != 1:
                    pairCount += 1
                    type(kicker)
                    type(numList[x])
                    if int(numList[x]) > int(kicker):
                        kicker = numList[x]
                    logger.debug(f'{numList[x]} is equal to: {numList[y]}')
                    logger.debug(f'PAIRCOUNTADDED to {pairCount} on iteration x: {x} y: {y}')
                    pairList.append(x)
                z = 0
    logger.debug(f'the pairCount is: {pairCount}')
    pairCount = pairCount / 2
    if pairCount == 1:
        logger.debug('PAIRCHECK RETURNED 1')
        return(1)
    elif  pairCount >= 2:
        logger.debug('PAIRCHECK RETURNED 2')
        return(2)

def straightCheckv3(card1, card2, tableList, playerNum, k):
    numTrue = 0
    numList = []
    tableCards = copy.deepcopy(tableList)
    tableCards.append(card1)
    tableCards.append(card2)
    sorted(tableCards)
    for i in range(len(tableCards)):
        if tableCards[i][1] == '0':
            numList.append(10)
        elif tableCards[i][1] == 'J':
            numList.append(11)
        elif tableCards[i][1] == 'Q':
            numList.append(12)
        elif tableCards[i][1] == 'K':
            numList.append(13)
        elif tableCards[i][1] == 'A':
            numList.append(14)
        else:
            numList.append(int(tableCards[i][1]))
    numList = list(set(numList))
    while len(numList) < 7:
        numList.append(999)
    numList.sort()

    for a in range(3):
        numTrue = 0
        if numList[-1 - a] - numList[-2 - a] == 1:
            kicker = numList[-1]
            numTrue += 1
            for b in range(4):
                if numList[-1 - a - b] - numList[-2 - a - b] == 1:
                    numTrue += 1
                    if numTrue == 5:
                        if k == 1:
                            return(kicker)
                        else:
                            return(True)

def threeCheck(card1, card2, tableList, playerNum):
    global kicker
    numList = []
    tableCards = copy.deepcopy(tableList)
    tableCards.append(card1)
    tableCards.append(card2)
    sorted(tableCards)
    for i in range(len(tableCards)):
        if tableCards[i][1] == '0':
            numList.append(10)
        elif tableCards[i][1] == 'J':
            numList.append(11)
        elif tableCards[i][1] == 'Q':
            numList.append(12)
        elif tableCards[i][1] == 'K':
            numList.append(13)
        elif tableCards[i][1] == 'A':
            numList.append(14)
        else:
            numList.append(int(tableCards[i][1]))
    numList.sort()
    logger.debug(f'threeCheck tablecards: {numList}')
    for i in range(len(numList)):
        if numList.count(numList[i]) == 3:
            kicker = numList[i]
            return True



def fourCheck(card1, card2, tableList, playerNum):
    global kicker
    numList = []
    tableCards = copy.deepcopy(tableList)
    tableCards.append(card1)
    tableCards.append(card2)
    sorted(tableCards)
    for i in range(len(tableCards)):
        if tableCards[i][1] == '0':
            numList.append(10)
        elif tableCards[i][1] == 'J':
            numList.append(11)
        elif tableCards[i][1] == 'Q':
            numList.append(12)
        elif tableCards[i][1] == 'K':
            numList.append(13)
        elif tableCards[i][1] == 'A':
            numList.append(14)
        else:
            numList.append(int(tableCards[i][1]))
    numList.sort()
    logger.debug(f'fourCheck tableCards list: {tableCards}')
    for i in range(len(numList)):
        if numList.count(numList[i]) == 4:
            kicker = numList[i]
            return True

def houseCheck(card1, card2, tableList, playerNum):
    numList = []
    temp = 0
    global kicker
    kicker = 0
    numList = []
    tableCards = copy.deepcopy(tableList)
    tableCards.append(card1)
    tableCards.append(card2)
    for i in range(len(tableCards)):
        if tableCards[i][1] == '0':
            numList.append(10)
        elif tableCards[i][1] == 'J':
            numList.append(11)
        elif tableCards[i][1] == 'Q':
            numList.append(12)
        elif tableCards[i][1] == 'K':
            numList.append(13)
        elif tableCards[i][1] == 'A':
            numList.append(14)
        else:
            numList.append(int(tableCards[i][1]))
    numList.sort()

    for a in range(5):
        if numList[6 - a] == numList[4 - a]:
            kicker = numList[4 - a]
            for b in range(3):
                numList.remove(numList[4 - a])
            temp = 1
            break

    if temp == 1:
        numList.sort(reverse=True)
        for c in range(len(numList)):
            pairCount = 0
            for d in range(len(numList)):
                if numList[c] == numList[d]:
                    pairCount += 1
                    if pairCount > 1:
                        return True


def winMain(card1, card2, tableCards, playerNum):
    global scoreList
    score = 0
    kicker = 0
    #FourCheck, score = 4
    
    if fourCheck(card1, card2, tableCards, playerNum) == True:
        scoreList[playerNum - 1].append(kicker)
        score = 4
        return score

    #StraightCheck, score = 6
    if straightCheckv3(card1, card2, tableCards, playerNum, 1) == 14 and flushCheck(card1, card2, tableCards, playerNum) == True:
        return 8
    elif flushCheck(card1, card2, tableCards, playerNum) == True:
        return 7
    elif straightCheckv3(card1, card2, tableCards, playerNum, 0) == True:
        return 6
    #FlushCheck, score = 7
    #StraightFlushCheck, score = 8

    #RoyalCheck, score = 9

    #FullCheck, score = 5
    if houseCheck(card1, card2, tableCards, playerNum) == True:
        scoreList[playerNum - 1].append(kicker)
        return 5

    #ThreeCheck, score = 3
    if threeCheck(card1, card2, tableCards, playerNum) == True:
        scoreList[playerNum - 1].append(kicker)
        score = 3
        return score
    
    #PairCheck, score = 1 or 2
    if pairCheck(card1, card2, tableCards, playerNum) == 1:
        scoreList[playerNum - 1].append(kicker)
        return 1
    elif pairCheck(card1, card2, tableCards, playerNum) == 2:
        scoreList[playerNum - 1].append(kicker)
        return 2

    return int(0)

def kickerCheck():
    logger.debug('a')