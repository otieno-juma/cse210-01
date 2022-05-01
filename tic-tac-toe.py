'''
Tic-Tac-Toe: A Solution
Author: Otieno Paul juma
'''
# create the board using a dictionary with initial values empty
from pip import main
from pyray import draw_billboard


g_board = {'7' : ' ' , '8': ' ' , '9': ' ' , 
         '4': ' ' , '5': ' ' , '6': ' ' ,
         '1': ' ' , '2': ' ' , '3': ' ' }
        
board_k = []

for k in g_board:
    board_k.append(k)

# print the updated board after each 

def game_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# definee the main
def main():

    turn = 'x'
    count = 0

    for i in range (10):
        game_board(g_board)
        print("it's your turn,"+ turn + ".make a move now?")

        move = input()

        if g_board[move] == " ":
            g_board[move] = turn
            count += 1

        else:
            print("space already filled.choose another spot?")
            continue

        # check for the winner
        if count >= 5:
            if g_board['7'] == ['8'] == g_board['9'] != ' ':
                game_board(g_board)
                print("Game over")
                print("***" + turn + "Won ***")
                break
            elif g_board['4'] == ['5'] == g_board['6'] != ' ':
                game_board(g_board)
                print("Game over")
                print("***" + turn + "Won ***")
                break
            elif g_board['1'] == ['2'] == g_board['3'] != ' ':
                game_board(g_board)
                print("Game over")
                print("***" + turn + "Won ***")
                break
            # if the board is full and neither player_1 nor player_2 has won the game declare draw
        if count == 9:
            print("***Game Over***")
            print("You made a Tie")

        # Allow player_2 to play each time player_1 makes a move
        if turn =='x':
            turn = '0'
        else:
            turn = 'x'

    # Ask players if they want to restart the game
    replay = input("would you like to play again (y/n)? ")
    replay.lower()
    if replay == 'y':
        for k in board_k:
            g_board[k] = " "

        main()


if __name__ == "__main__":
    main()