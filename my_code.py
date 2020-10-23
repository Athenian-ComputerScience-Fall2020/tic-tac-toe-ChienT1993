# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  
# A note on style: Dictionaries can be defined before or after functions.
board = {'TL': '', 'TM': '', 'TR': '', 'ML': '', 'M': '', 'MR': '', 'BL': '', 'BM': '', 'BR': ''}
position = ['TL', 'TM', 'TR', 'ML', 'M', 'MR', 'BL', 'BM', 'BR']
def tictactoe(board):
    print (" " + board['TL'] + " | " + board['TM'] + " | " + board['TR'] + " ")
    print ("---+---+---")
    print (" " + board['ML'] + " | " + board['M'] + " | " + board['MR'] + " ")
    print ("---+---+---")
    print (" " + board['BL'] + " | " + board['BM'] + " | " + board['BR'] + " ")
print ("There are 9 squares on the board, each has a name based on its position.")
tictactoe(board)

