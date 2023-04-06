import copy
import logging
logging.basicConfig(filename='pokerWin.log', encoding='utf-8', level=logging.INFO)

kicker = 0
scoreList = [[],[],[],[]]

def flushCheck(card1, card2, tableList, playerNum):
    tableCards = copy.deepcopy(tableList)
    colorList = [[],[],[],[]]
    tableCards.append(card1)
    tableCards.append(card2)
    sorted(tableCards)
    logging.info(f'flushDeck tableCards: {tableCards}')
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
        logging.info("This is probably a flush")
        logging.info(len(colorList[0]))
        logging.info(len(colorList[1]))
        logging.info(colorList)
        return True
    else:
        logging.info("This probably isn't a flush")
        logging.info(len(colorList[0]))
        logging.info(len(colorList[1]))
        logging.info(colorList)

def pairCheck(card1, card2, tableList, playerNum):
    global kicker
    tableCards = copy.deepcopy(tableList)
    pairCount = 0
    numList = []
    pairList = []
    tableCards.append(card1)
    tableCards.append(card2)
    sorted(tableCards)
    logging.info(f'pairCheck tableCards: {tableCards}')
    for i in range(len(tableCards)):
        numList.append(tableCards[i][1])
    sorted(numList)
    for x in range(len(numList)):
        logging.info(f'**paircheck key value "x": {x}', f'and the card num in question is: {numList[x]}', '\n', f'and the tableCards[x] value is: {tableCards[x]}')
        z = 1
        for y in range(len(numList)):
            logging.info(f'**paircheck key value "y": {y}' f'and the card num in question is: {numList[x]}', '\n', f'and the tableCards[y] value is: {tableCards[y]}')
            if numList[x] == numList[y]:
                if z != 1:
                    pairCount += 1
                    logging.info(f'{numList[x]} is equal to: {numList[y]}')
                    logging.info(f'PAIRCOUNTADDED to {pairCount} on iteration x: {x} y: {y}')
                    pairList.append(x)
                z = 0
    logging.info(f'the pairCount is: {pairCount}')
    pairCount = pairCount / 2
    if pairCount == 1:
        kicker = max(tableCards)
        logging.info('PAIRCHECK RETURNED 1')
        return(1)
    elif  pairCount >= 2:
        kicker = max(tableCards)
        logging.info('PAIRCHECK RETURNED 2')
        return(2)

def straightCheckv2(card1, card2, tableList, playerNum):
    global kicker
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
    print(f"straightCheck2 debug: numList = {numList}")
    sorted(numList)

    for b in range(2):
        if numList[0+b] < numList[4+b]:
            logging.info(f"Straight from {numList[0 + b]} to {numList[4+b]}")
            numtrue = 0
            for o in range(4):
                if numList[4 + b] - numList[4 + b - o] == 1:
                    numTrue += 1
            if numTrue == 5:
                kicker = numList[4+b]
                return(True)

def straightCheck(card1, card2, tableList, playerNum):
    global kicker
    tableTemp = []
    tableCards = copy.deepcopy(tableList)
    tableCards.append(card1)
    tableCards.append(card2)
    sorted(tableCards)
    logging.info(f'straightCheck tableCards: {tableCards}')
    for i in range(len(tableCards)):
        logging.info(tableCards)
        logging.info(f'i is: i')
        logging.info(f'range(len(tablecards)) is equal to {range(len(tableCards))}')
        logging.info(f'tableCards of i is: {tableCards[i]}')

        try: tableCards[i] = int(tableCards[i][1])
        except ValueError:
            tableCards[i] = tableCards[i][1]
        if tableCards[i] == "J":
            tableCards.pop(i)
            tableCards.insert(0, int(11))
        elif tableCards[i] == "Q":
            tableCards.pop(i)
            tableCards.insert(0, int(12))
        elif tableCards[i] == "K":
            tableCards.pop(i)
            tableCards.insert(0, int(13))
        elif tableCards[i] == "A":
            tableCards.pop(i)
            tableCards.insert(0, int(14))
    sorted(tableCards)
    logging.info(f'tablecards list is: {tableCards}')
    if int(tableCards[-1]) -1 == tableCards[6]:
        logging.info("string will start here.")
    for b in range(2):
        if tableCards[0+b] < tableCards[4+b]:
            logging.info(f"Straight from {tableCards[0 + b]} to {tableCards[4+b]}")
            kicker = tableCards[4+b]
            return(True)

def threeCheck(card1, card2, tableList, playerNum):
    global kicker
    numList = []
    tableCards = copy.deepcopy(tableList)
    tableCards.append(card1)
    tableCards.append(card2)
    sorted(tableCards)
    for i in range(len(tableCards)):
        numList.append(tableCards[i][1])
    sorted(numList)
    logging.info(f'threeCheck tablecards: {numList}')
    for i in range(len(numList)):
        print(f"threeCheck debug: i = {i}, tableCards[i] = {tableCards[i]}, tableCards.count(tableCards[i]) = {tableCards.count(tableCards[i])}")
        if numList.count(numList[i]) == 3:
            kicker = max(tableCards)
            return True



def fourCheck(card1, card2, tableList, playerNum):
    global kicker
    numList = []
    tableCards = copy.deepcopy(tableList)
    tableCards.append(card1)
    tableCards.append(card2)
    sorted(tableCards)
    for i in range(len(tableCards)):
        numList.append(tableCards[i][1])
    sorted(numList)
    logging.info(f'fourCheck tableCards list: {tableCards}')
    for i in range(len(numList)):
        if tableCards.count(numList[i]) == 4:
            kicker = max(numList)
            return True

def houseCheck(card1, card2, tableList, playerNum):
    global kicker
    numList = []
    tableCards = copy.deepcopy(tableList)
    tableCards.append(card1)
    tableCards.append(card2)
    sorted(tableCards)
    for i in range(len(tableCards)):
        numList.append(tableCards[i][1])
    sorted(numList)
    logging.info(f'houseCheck tableCards:  {tableCards}')
    tempKick = max(numList)
    for i in range(len(numList)):
        if numList.count(i) == 3:
            kicker = max(numList)
            for a in range(3):
                numList.remove(numList[i])
            for a in range(len(numList)):
                if numList.count(i) == 2:
                    kicker = tempKick
                    return True


def winMain(card1, card2, tableCards, playerNum):
    global scoreList
    score = 0
    #FourCheck, score = 4
    
    if fourCheck(card1, card2, tableCards, playerNum) == True:
        scoreList[playerNum - 1].append(kicker)
        score = 4
        return score

    #StraightCheck, score = 6
    if straightCheckv2(card1, card2, tableCards, playerNum) == True and flushCheck(card1, card2, tableCards, playerNum) == True:
        return 8
    elif flushCheck(card1, card2, tableCards, playerNum) == True:
        return 7
    elif straightCheckv2(card1, card2, tableCards, playerNum) == True:
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
    logging.info('a')