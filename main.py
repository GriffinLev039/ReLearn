import random
import winCheck
import logging
import time
import logging.handlers

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
info_handler = logging.FileHandler('pokerINFO.log', mode='w')

info_handler.setLevel(logging.INFO)
info_formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
info_handler.setFormatter(info_formatter)
logger.addHandler(info_handler)

debug_handler = logging.FileHandler('pokerDEBUG.log', mode='w')
debug_handler.setLevel(logging.DEBUG)
debug_formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
debug_handler.setFormatter(debug_formatter)
logger.addHandler(debug_handler)

logger.info('****')
logger.info('****')
logger.info("NEW INSTANCE")
logger.info('****')
logger.info('****')

playerScore = []
cardDeck = []
cardSuits = ["C", "S", "D", "H"]
cardNums = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "0", "J","K","Q"]
cardTable = []
tempList = []
burnList = []
tableList = []
playerBets = []
playerWallets = []
playerCount = 0
potTotal = int(0)
potTop = 0
y = 0
a = 0
print(len(cardDeck))
for x in range(len(cardNums)):
    y = 0
    while y < 4:
        z = cardSuits[y] + cardNums[x]
        cardDeck.append(z)
        y = y + 1

print(cardDeck)
print(len(cardDeck))

#
#
#
def userInput():
    while True:
        playerCount = input("How many players are you playing with? (1-4, numerical only):")
        try:
            playerCount = int(playerCount)
            if playerCount <= 0 or playerCount > 4:
                print("Illegitimate playercount.")
            else:
                print("All good.")
                return playerCount

        except ValueError:
            print("Please enter in a numerical format only.")
#
#
#
def chipInput():
    while True:
        chipCount = input("How many chips should each player get? Enter a numerical value only:")
        try:
            chipCount = int(chipCount)
            if chipCount <= 0:
                print("Illegitimate chip count.")
            else:
                print("All good.")
                return chipCount

        except ValueError:
            print("Please enter in a numerical format only.")

#
#
#
def cardDeal(var1):
    a = 0
    c = 0
    global burnList

    lists = [[] for _ in range(var1)]
    for a in range(len(lists)):
        for i in range(2):
            c = len(cardDeck) - 1
            cardNum = random.randint(0, c)
            lists[a].append(str(cardDeck[cardNum]))
            burnList.append(cardDeck[cardNum])
            cardDeck.pop(cardNum)
    print(lists)
    print(burnList)
    return lists

#
#
#
def dealerFunc(o):
    global tableList
    for i in range(o):
        c = len(cardDeck) - 1
        cardNum = random.randint(0, c)
        tableList.append(str(cardDeck[cardNum]))
        burnList.append(cardDeck[cardNum])
        cardDeck.pop(cardNum)

#
#
#
def playerTurn(playerNum):
    temp = 0
    global potTotal
    global potTop
    print("Your cards are: ", playerHands[playerNum][0], 'and', playerHands[playerNum][1])
    if len(playerHands[playerNum]) == 0:
        print('Player has folded, turn will be skipped.')
        return
    while True:
        if potTop == 0:
            player = int(input("What do you want to do? 1 for fold, 2 for check or 3 for bet:"))
            if player == 4:
                player = 5
        else:
            player = int(input("What do you want to do? 1 for fold, 2 for call, or 3 for raise:"))
            temp = 1
            if player == 3:
                player = 4
        try:

            if player == 4:
                decision = 'raise.'
                while True:
                    raiseNum = input('How much do you want to raise to?')
                    print("The current top bet is", potTop, 'chips.')
                    try:
                        raiseNum = int(raiseNum)
                        if raiseNum > playerWallets[playerNum]:
                            raise ValueError
                        elif raiseNum < potTop:
                            raise ValueError
                        else:
                            potTop = raiseNum
                            potTotal = potTop + potTotal
                            playerWallets[playerNum] = playerWallets[playerNum] - raiseNum
                            break

                    except ValueError:
                        print("Please enter a valid numerical value only. Remember, you have", playerWallets[playerNum], 'chips.')
                        print("The current top bet is", potTop, 'chips.')


            elif player == 3:
                decision = 'bet.'
                while True:
                    raiseNum = input('How much do you want to bet?')
                    try:
                        raiseNum = int(raiseNum)
                        if raiseNum > playerWallets[playerNum]:
                            raise ValueError
                        elif raiseNum < potTop:
                            raise ValueError
                        else:
                            potTop = raiseNum
                            potTotal = potTop + potTotal
                            playerWallets[playerNum] = playerWallets[playerNum] - raiseNum
                            break

                    except ValueError:
                        print("Please enter a valid numerical value only. Remember, you have", playerWallets[playerNum], 'chips.')

            elif player == 2:
                if temp != 1:
                    decision = 'check.'
                else:
                    decision = 'call.'
                while True:
                    if potTop == 0:
                        break
                    elif playerWallets[playerNum] >= potTop:
                        potTotal = potTotal + potTop
                        playerWallets[playerNum] = playerWallets[playerNum] - potTop
                        break
                    elif playerWallets[playerNum] <= potTop:
                        print("You are now all in.")
                        potTotal = potTotal + playerWallets[playerNum]
                        playerWallets[playerNum] = 0
                        break


            elif player == 1:
                decision = 'fold.'
                for i in range(2):
                    burnList.append(playerHands[playerNum])
                    playerHands[playerNum].pop(i - 1)


            print('You have chosen to', decision)
            break

        except ValueError:
            print("Please only enter 1, 2, 3, or 4")


def chipSort(scoreList, pot, wallets):
    winnerList = []
    for a in range(len(playerScore)):
        k = 0
        for b in range(len(playerScore)):
            if playerScore[a] == playerScore[b]:
                if k == 1:
                    winnerList.append(a)
                k = 1
    pot = pot/(len(winnerList)/2)
    for c in range(len(winnerList)):
        wallets[winnerList[a]] = wallets[winnerList[a]] + pot
        print(f'player {a} has won and now has {wallets[a]} chips!')
    print(f'winnerlist is: {winnerList}')
    print(f'wallets is: {wallets}')
    return wallets

playerCount = userInput()
#playerHands = cardDeal(playerCount)
chipCount = chipInput()
for i in range(playerCount):
    playerWallets.append(chipCount)
print(playerWallets)

doPlay = 1

while doPlay == 1:
    logger.info('****')
    logger.info("NEW ROUND")
    logger.info('****')
    playerHands = cardDeal(playerCount)
    for i in range(playerCount):
        playerTurn(i)
    dealerFunc(3)
    print(tableList)
    potTotal = potTotal + potTop
    potTop = 0

    for i in range(playerCount):
        playerTurn(i)
    dealerFunc(1)
    print(tableList)
    potTotal = potTotal + potTop
    potTop = 0

    for i in range(playerCount):
        playerTurn(i)
    dealerFunc(1)
    print(tableList)
    potTotal = potTotal + potTop
    potTop = 0

    for i in range(playerCount):
        playerTurn(i)

    for i in range(playerCount):
        if len(playerHands[i]) == 0:
            playerScore.append(0)
        else:
            playerScore.append(winCheck.winMain(playerHands[i][0],playerHands[i][1],tableList,i))
    print('playerScore is: ', playerScore)
    # for a in range(len(playerScore)):
    #     if set(playerScore[a]) >= 1:
    #         print('checking for kicker card, since there is a tie...')
    #         print('score list is:', playerScore)
    #         winCheck.kickerCheck()
    print("The playerHands are: ", playerHands)
    print("The table cards are: ", tableList)
    chipSort(playerScore, potTotal, playerWallets)
    # print("the winner is, Player", int(playerScore.index(max(playerScore))) + 1)
    for b in range(playerCount):
        logging.debug(f'Player {b + 1} now has {chipCount[b]} chips.')
        if chipCount == 0:
            print(f'Player {b + 1} has lost.')

    logger.info(f'playerScore is:  {playerScore}')
    logger.info(f'the playerHands are: {playerHands}')
    logger.info(f'The table cards are: {tableList}')
    logger.info(f'The winner is, Player: {int(playerScore.index(max(playerScore))) + 1}')
    doPlay = int(input("Do you want to play again? 1 for yes, 0 for no: "))
    if doPlay == 0:
        break
    else:
        playerHands = [[],[],[],[]]
        burnList = []
        playerList = []
        potTotal = int(0)
        potTop = 0
        playerScore = []
        cardDeck = []
        cardTable = []
        tempList = []
        tableList = []
        playerBets = []
        print(len(cardDeck))
        for x in range(len(cardNums)):
            y = 0
            while y < 4:
                z = cardSuits[y] + cardNums[x]
                cardDeck.append(z)
                y = y + 1
    time.sleep(.001)
