# Tic Tac Toe with AI
# Create the diameters for the board
board = [" " for x in range(10)]

# Create the board


def board_layout(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

# function to insert a letter (x or o)


def insert_letter(letter, position):
    board[position] = letter

# Check if space is free


def free_space(position):
    return board[position] == " "


# Winning condiiton based on if Letter (l) equals letter position (lp)

def winner(l, lp):
    # First Row                                      #Second Row                                 #Third Row                                  #Diagonal                                        #Diagonal                                  #First Column                                   #Second Column                                  #Third Column
    return (l[1] == lp and l[2] == lp and l[3] == lp) or (l[4] == lp and l[5] == lp and l[6] == lp) or (l[7] == lp and l[8] == lp and l[9] == lp) or (l[1] == lp and l[5] == lp and l[9] == lp) or (l[3] == lp and l[5] == lp and l[7] == lp) or (l[1] == lp and l[4] == lp and l[7] == lp) or (l[2] == lp and l[5] == lp and l[8] == lp) or (l[3] == lp and l[6] == lp and l[9] == lp)


# Logic for your move
def player_turn():
    active = True
    while active:
        move = input("Select a position (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if free_space(move):
                    active = False
                    insert_letter('X', move)
                else:
                    print("That Space has been taken")
            else:
                print("Select a position (1-9): ")

        except:
            print("Enter a position between 1-9")

# Logic for the computers turn
# Check the board for any open spaces
# Follow the basic tic tac toe algorithm or in other words the logic to always win tic tac toe, I found it online at "https://youtu.be/5n2aQ3UQu9Y"


def computers_turn():
    possible_moves = [x for x, letter in enumerate(
        board) if letter == " " and x != 0]
    move = 0

    # Check who wins
    for letter in ['O', 'X']:
        for i in possible_moves:
            new_board = board[:]
            new_board[i] = letter
            # Check if the new_board will win, if it does then thats the move to take for the computer
            if winner(new_board, letter):
                move = i
                return move

    # Check if any corners are oopen
    open_corners = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            open_corners.append(i)

    # Randomly select one of the corners to move into
    if len(open_corners) > 0:  # This should work only if the list is greater than zero, this should avoid an error occuring because the computer won't be able to select from an empty list
        move = random(open_corners)
        return move

    # If the middle is open then the computer should take it
    if 5 in possible_moves:
        move = 5
        return move

    # Check if any edges are oopen
    open_edges = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            open_edges.append(i)

    # Randomly select one of the edges to move into
    if len(open_edges) > 0:  # This should work only if the list is greater than zero, this should avoid an error occuring because the computer won't be able to select from an empty list
        move = random(open_edges)

    return move

# Get a random move


def random(li):
    import random
    length = len(li)
    r = random.randrange(0, length)
    return li[r]

# Checks to see if the board is full


def is_full(board):
    if board.count(" ") > 1:
        return False
    else:
        return True


def main():
    print("Welcome to Tic Tac Toe")
    board_layout(board)

    while not(is_full(board)):
        # If the computer wins
        if not(winner(board, 'O')):
            player_turn()
            board_layout(board)
        else:
            print("The computer won! Better luck next time.")
            break

        # If you win
        if not(winner(board, 'X')):
            move = computers_turn()
            if move == 0:
                print("Tie!")
            else:
                insert_letter("O", move)
                print("Computer placed an 'O' in position", move, ".")
                board_layout(board)
        else:
            print("You Won!")
            break

    # If the game is a tie
    if is_full(board):
        print("You guys both won...TIE")


while True:

    user_input = input("Play Tic-Tac-Toe? (yes/no) ")
    if user_input == "yes":
        main()
    else:
        print("Okay, Goodbye!")
        break
