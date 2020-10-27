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
        elif turn != random_int:#seems like any number other then 1 or 2 also count as a number different from the random_int
            print (player_2, "(O) go first and " + player_1 + " (X) go second")
    except:
        print ("Please either type 1 or 2")
        go_first(player_1, player_2)

def strike():
    print ("Here are the options for your strike's position:")
    print (position)
    x = input("Which position do you want to strike?: ")
    position.remove(x)
    print (player_1, "is X and " + player_2, "is O")
    y = input("What is your symbol (X or O)?: ")
    board[x] = y
    tictactoe(board)
    strike()
    
def win():
    strike()
    if board['TL'] == 'X' and board['TM'] == 'X' and board['TR'] == 'X':#WHY NOT STOP
        print (player_1, "win!")
        exit()
    

player_1 = input("Player 1, please type your name here: ")
player_2 = input("Player 2, please type your name here: ")
go_first(player_1,player_2)
win()

