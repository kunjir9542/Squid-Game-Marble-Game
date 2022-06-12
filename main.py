from random import randint

playerMarbles = 10
computerMarbles = 10
turn = randint(0, 1)


def titleScreen():
    print("-----------------------------------------------------------------------------------------------------")
    beginning = input(
        "Hello, and welcome to the Marble Game from Squid Game! Press E to start and R to read the rules (E/R)")

    if beginning == "R":
        print("-----------------------------------------------------------------------------------------------------")
        print("Both you and the computer will start with 10 marbles.")
        print("At the start of each round, both you and the computer will bet a certain number of marbles.")
        print(
            "The player and the computer will each alternate guessing whether the number of marbles they bet are even or odd each round.")
        print("If the player guesses right, they receive the amount of marbles the computer bet.")
        print("If the player guesses wrong, no one receives any marbles and the round is over")
        print("This is repeated until a player has 0 marbles left, and if this happens, that said player loses. Have fun!")
        titleScreen()
    if beginning == "E":
        startGame()

def startGame():
    global turn
    if turn == 0:
        playerTurn()
    elif turn == 1:
        computerTurn()

def playerTurn():
    global playerMarbles
    global computerMarbles
    global turn
    print("-----------------------------------------------------------------------------------------------------")
    print("It is your turn!")
    print("You have " + str(playerMarbles) + " marbles remaining")
    print("The computer has " + str(computerMarbles) + " marbles remaining")
    betMarbles = input("How many marbles do you want to bet?")
    if betMarbles.isnumeric() and int(betMarbles) <= playerMarbles:
        print("-----------------------------------------------------------------------------------------------------")
        print("You bet " + betMarbles + " marbles")
        computerGuess = randint(0, 1)
        if computerGuess == 0:
            print("The computer guessed even")
            if int(betMarbles) % 2 == 0:
                print("The computer guessed right! It took your bet marbles")
                playerMarbles -= int(betMarbles)
                computerMarbles += int(betMarbles)
            else:
                print("The computer guessed wrong! You are safe")
        else:
            print("The computer guessed odd")
            if int(betMarbles) % 2 == 1:
                print("The computer guessed right! It took your bet marbles")
                playerMarbles -= int(betMarbles)
                computerMarbles += int(betMarbles)
            else:
                print("The computer guessed wrong! You are safe")
        if checkWinner():
            turn = 2
        else:
            turn = 1
            startGame()
    else:
        print("You must have typed something wrong. Please try again")
        playerTurn()
def computerTurn():
    global playerMarbles
    global computerMarbles
    global turn
    print("-----------------------------------------------------------------------------------------------------")
    print("It is the computer's turn")
    print("You have " + str(playerMarbles) + " marbles remaining")
    print("The computer has " + str(computerMarbles) + " marbles remaining")
    betMarbles = randint(1, computerMarbles)
    playerGuess = input("The computer bet its marbles. Do you think it is odd or even? (O/E)")
    if playerGuess == "E":
        print("You guessed even")
        if int(betMarbles) % 2 == 0:
            print("You guessed right! You took their bet marbles")
            playerMarbles += int(betMarbles)
            computerMarbles -= int(betMarbles)
        else:
            print("You guessed wrong! They are safe")
    elif playerGuess == "O":
        print("You guessed odd")
        if int(betMarbles) % 2 == 1:
            print("You guessed right! You took their bet marbles")
            playerMarbles += int(betMarbles)
            computerMarbles -= int(betMarbles)
        else:
            print("You guessed wrong! They are safe")
    else:
        print("You must have typed something wrong. Please try again")
        computerTurn()
    if checkWinner():
        turn = 2
    else:
        turn = 0
        startGame()

def checkWinner():
    global playerMarbles
    global computerMarbles
    someoneWon = False
    if playerMarbles == 0:
        print("-----------------------------------------------------------------------------------------------------")
        print("You Lost!")
        someoneWon = True
    elif computerMarbles == 0:
        print("-----------------------------------------------------------------------------------------------------")
        print("You Won!")
        someoneWon = True
    return someoneWon

titleScreen()