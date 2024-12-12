from IPython.display import clear_output

def display_board(board):
    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

#asking user 1 to choose 0 or x that he will play 

def user_choice():
    choice="NO"
    ''' 
    output= player1 , player 2
    '''
    while choice not in ['O','X']:
        choice= input("Player 1! Choose what you want to play with (X OR O):").upper()
        print("WRONG INPUT!")

        player1=choice
        if player1=='X':
            player2='O'
        else:
            player2='X'
    return (player1,player2)

def place_marker(board,marker,position):
    board[position]=marker


def win_check(board,marker):
    #WIN Condition

    #All Rows
    return((board[1]==marker and board[2]==marker and board[3]==marker) or
    (board[4]==board[5]==board[6]==marker) or 
    (board[7]==board[8]==board[9]==marker) or
           #All Columns
    (board[1]==board[4]==board[7]==marker) or
    (board[2]==board[5]==board[8]==marker) or
    (board[3]==board[6]==board[9]==marker) or
        #2 Diagonal   
    (board[1]==board[5]==board[9]==marker) or
    (board[3]==board[5]==board[7]==marker))
    

#Randomize which player will go first
import random

def choose_first():
    flip=random.randint(0,1)
    if flip==1:
        return 'Player 1'
    else:
        return 'player 2'

#Now check in the list if any box is still available or not ie box is freely available 

def space_check(board,position):
    return board[position]== ' '


#check if the board is full and if full then return a boolean true or false if any box empty

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i)==True:
            return False
    #if the board is full return True
    return True

def player_choice(board):
    position = '0'

    while position not in [1,2,3,4,5,6,7,8,9] or  not space_check(board,position):
        position=int(input('Input a position (1-9):'))

    return position

def play_again():
    choice=' '
    while choice not in ['YES','NO']:
        choice=input("Wants to Challenge Again ? YES or NO").upper()
    return choice=='YES'

# print welcome message 

print("Welcome to Tic Tac Toe")

while True:
    
    #board setup 
    the_board=[' ']*10
    #PLAY GAME 

    #sET EVERYTHING LIKE BOARD->WHO'S FIRST -> MARKER 
    #board setup 
    the_board=[' ']*10
    player1_choice,player2_choice=user_choice()

    turn=choose_first()
    print(turn + ' will go first')

    play_game=input("Ready to play ? y Or n").lower()
    if play_game=='y':
        game_on=True
    else:
        game_on=False
        
    #PLAY
    while game_on==True:
        if turn=='Player 1':
            #PLAYER ONE TURN

            #DISPLAY THE BOARD TO THE PLAYER ONE 
            display_board(the_board)
            #choose a position
            position=player_choice(the_board)
            #place the marker into the position 
            place_marker(the_board,player1_choice,position)

            #Check if win 
            if win_check(the_board,player1_choice)==True:
                display_board(the_board)
                print("Player 1 won this game!")
                game_on=False
            else:
                if full_board_check(the_board)==True:
                    display_board(the_board)
                    print("GAME TIE!")
                    game_on=False
                else:
                    turn='Player 2'
        else:
            #display the board
            display_board(the_board)
            #choose the position
            position=player_choice(the_board)
            
            #place the marker
            place_marker(the_board,player2_choice,position)

            #check if won
            if win_check(the_board,player2_choice)==True:
                display_board(the_board)
                print("Player 2 Won!")
                game_on=False
            else:
                if full_board_check(the_board)==True:
                    display_board(the_board)
                    print("GAME TIE !")
                    game_on=False
                else:
                    turn='Player 1'
            
        
            
    if not play_again():
        break 
    #BREAK OUT OF THE WHILE LOOP ON REPLAY()