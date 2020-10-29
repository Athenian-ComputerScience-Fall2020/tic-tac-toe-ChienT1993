# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  
# A note on style: Dictionaries can be defined before or after functions.
import random

board = {'TL': ' ', 'TM': ' ', 'TR': ' ', 'ML': ' ', 'M': ' ', 'MR': ' ', 'BL': ' ', 'BM': ' ', 'BR': ' '}
position = ['TL', 'TM', 'TR', 'ML', 'M', 'MR', 'BL', 'BM', 'BR']

def tictactoe(board):#the board
    print (" " + board['TL'] + " | " + board['TM'] + " | " + board['TR'] + " ")
    print ("---+---+---")
    print (" " + board['ML'] + " | " + board['M'] + " | " + board['MR'] + " ")
    print ("---+---+---")
    print (" " + board['BL'] + " | " + board['BM'] + " | " + board['BR'] + " ")

def go_first(player_1, player_2):
    random_int = random.randint(1,2)
    try:
        turn = int(input(player_1 + " choose either 1 or 2: "))
        if turn == random_int:
            print (player_1, "(X) go first and " + player_2 + " (O) go second")
        elif turn != random_int and turn < 3:#seems like any number other then 1 or 2 also count as a number different from the random_int
            print (player_2, "(X) go first and " + player_1 + " (O) go second")
    except:
        print ("Please either type 1 or 2")
        go_first(player_1, player_2)

def strike_X(strikes):#strike and win
    print ("Here are the options for your strike's position:")
    print (position)
    x = input("Which position do you want to strike?: ")
    position.remove(x)
    board[x] = 'X'
    strikes = strikes + 1
    tictactoe(board)
    if board['TL'] == 'X' and board['TM'] == 'X' and board['TR'] == 'X':#Side top
        print (player_1, "won!")
        exit()
    if board['ML'] == 'X' and board['M'] == 'X' and board['MR'] == 'X':#Side mid
        print (player_1, "won!")
        exit()
    if board['BL'] == 'X' and board['BM'] == 'X' and board['BR'] == 'X':#Side bot
        print (player_1, "won!")
        exit()
    if board['TL'] == 'X' and board['ML'] == 'X' and board['BL'] == 'X':#Down left
        print (player_1, "won!")
        exit()
    if board['TM'] == 'X' and board['M'] == 'X' and board['BM'] == 'X':#Down mid
        print (player_1, "won!")
        exit()
    if board['TR'] == 'X' and board['MR'] == 'X' and board['BR'] == 'X':#Down right
        print (player_1, "won!")
        exit()
    if board['TL'] == 'X' and board['M'] == 'X' and board['BR'] == 'X':#Cross
        print (player_1, "won!")
        exit()
    if board['TR'] == 'X' and board['M'] == 'X' and board['BL'] == 'X':#Cross
        print (player_1, "won!")
        exit()
    if strikes == 9:
        print ("It's a tie!")
        exit()
    else:
        strike_O(strikes)
    
def strike_O(strikes):#strike and win
    print ("Here are the options for your strike's position:")
    print (position)
    x = input("Which position do you want to strike?: ")
    position.remove(x)
    board[x] = 'O'
    strikes = strikes + 1
    tictactoe(board)
    if board['TL'] == 'O' and board['TM'] == 'O' and board['TR'] == 'O':#Side top
        print (player_1, "won!")
        exit()
    if board['ML'] == 'O' and board['M'] == 'O' and board['MR'] == 'O':#Side mid
        print (player_1, "won!")
        exit()
    if board['BL'] == 'O' and board['BM'] == 'O' and board['BR'] == 'O':#Side bot
        print (player_1, "won!")
        exit()
    if board['TL'] == 'O' and board['ML'] == 'O' and board['BL'] == 'O':#Down left
        print (player_1, "won!")
        exit()
    if board['TM'] == 'O' and board['M'] == 'O' and board['BM'] == 'O':#Down mid
        print (player_1, "won!")
        exit()
    if board['TR'] == 'O' and board['MR'] == 'O' and board['BR'] == 'O':#Down right
        print (player_1, "won!")
        exit()
    if board['TL'] == 'O' and board['M'] == 'O' and board['BR'] == 'O':#Cross
        print (player_1, "won!")
        exit()
    if board['TR'] == 'O' and board['M'] == 'O' and board['BL'] == 'O':#Cross
        print (player_1, "won!")
        exit()
    if strikes == 9:
        print ("It's a tie!")
        exit()
    else:
        strike_X(strikes)

strikes = 0
player_1 = input("Player 1, please type your name here: ")
player_2 = input("Player 2, please type your name here: ")
go_first(player_1,player_2)
strike_X(strikes)
