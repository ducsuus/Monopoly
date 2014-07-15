'''

General Playthrough:

    - Setup variables (properties, stats, etc)
    - Get players
    

'''


## Imports
from random import randint

## Variables

## Player Class
class Player:

    name = "UNDEFINED"

    token = "UNDEFINED"

    money = 100000.0

    isInJail = False

    position = 0

    def move(this, squares):

        this.position = (this.position + squares) % 40
    
## Square Class (each individual square on the board)
class Square:

    name = "UNDEFINED"

    isProperty = False

    price = 0.0

    owner = "none"

    owned = False

    rent = 0.0

    def setOwner(this, player):

        this.owner = player

        this.owned = True

    def removeOwner(this):

        this.owner = "none"

        this.owned = False
    
## Functions

def taxPlayer(player, square):

    player.money -= square.rent

    square.owner.money += square.rent

    return square.rent

def playTurn(player, square):

    diceScore = rollDice(0)

    if diceScore > 0:
        players[i].move(diceScore)
    else:
        # Player needs to go to jail now
        print("Player should be in jail")
    

    print(player.name + " (" + player.token + ") is on square " + str(player.position + 1) + " (" + square.name + ") \n")

    if square.owned == False:

        if square.price <= player.money:
            
            if input("This property is not currently owned, you have enough money to buy it, will you (y/n): ").upper() == "Y":

                player.money -= square.price

                square.setOwner(player)

                print("Bought property " + square.name + "!")

        else:

            print("This property is not currently owned, but you don't have enough money to buy it. Tough luck :(")

    else:
        print("This propery is currently owned, you payed " + str(taxPlayer(player, square)) + " to " + square.owner.name + ". You now have a balance of " + str(player.money) + ".")

        
        
        ##TODO: Tax

    input("Press Enter to continue...")

    

def clearScreen():
    print("\n" * 50)


def isExiting():

    return True if input("Carry On Playing (y/n): ").upper() == "N" else False


def getToken(_list, message):

    for i in range(0, len(_list)):
        print(str(i + 1) + ": " + str(_list[i]) + ", ")

    return int(input(message)) - 1


def loadBoard(fileLocation):

    squares = []

    with open(fileLocation) as f:
        lines = f.read().splitlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].split(", ")

        squares.append(Square())

        squares[i].name = str(lines[i][0])

        squares[i].isProperty = True if lines[i][1].upper() == "TRUE" else False

        squares[i].price = float(lines[i][2])


    return squares
    

# Get players
def getPlayers():

    availableTokens = ["Wheelbarrow", "Battleship", "Racing Car", "Thimble", "Boot", "Scottie Dog", "Top Hat", "Cat"]

    playerCount = int(input("How many players are playing? "))

    while playerCount > 8:

        print("Too many players, you can have up to a maximum of 8 players!")

        playerCount = int(input("How many players are playing? "))

    players = []

    for i in range(0, playerCount):
        players.append(Player())
        
        players[i].name = input("Player " + str(i + 1) + "'s Name: ")

        token = getToken(availableTokens, "Player " + str(i + 1) + "'s token: ")

        players[i].token = availableTokens.pop(token)

    return players


def rollDice(streak):

    if streak >= 3:
        return -1

    streak += 1

    dice1 = randint(0, 6)
    dice2 = randint(0, 6)

    total = dice1 + dice2

    if dice1 == dice2:
        total += rollDice(streak)

    return total


# Get the players
players = getPlayers()

# Get the board
board = loadBoard("Board.txt")

# Breakout variable
playing = True

## Main loop
while playing:

    clearScreen()

    for i in range(0, len(players)):

        playTurn(players[i], board[players[i].position])
        
    ##if isExiting():
    ##    playing = False

## Finished the game, let's leave a nice little message at the center of the player's screen :)
clearScreen()

print(" " * 38 + "Bye!")

print("\n" * 20)
    
