from time import sleep

def displayboard(board):
    print(" ", board[0][0], "│", board[0][1], "│", board[0][2])
    print(" ───┼───┼───")
    print(" ", board[1][0], "│", board[1][1], "│", board[1][2])
    print(" ───┼───┼───")
    print(" ", board[2][0], "│", board[2][1], "│", board[2][2])

def check_win(board, player):
    won = False
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        won = True
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        won = True
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        won = True
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        won = True
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        won = True
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        won = True
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        won = True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        won = True
    return won

def instructions(board):
    print("Welcome to noughts and crosses")
    print("------------------------------")
    sleep(1)
    print("Instructions:")
    print("")
    print("This is a 2 player game")
    print("The first player will be noughts")
    print("The second player will be crosses")
    print("The game is presented in a grid...")
    print("")
    sleep(5)
    displayboard(board)
    sleep(2)
    print("")
    print("To choose a position for your piece, enter the location number")
    print("")
    sleep(2)

def readpositions(player):
    positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print(f"{player}'s turn. Where would you like to place your piece?")
    position = input()
    while position not in positions:
        print("You must enter a number from 1 to 9")
        position = input()
    return position

def move(board, player):
    position = readpositions(player)
    if position == "1":
        board[0][0] = player
    elif position == "2":
        board[0][1] = player
    elif position == "3":
        board[0][2] = player
    elif position == "4":
        board[1][0] = player
    elif position == "5":
        board[1][1] = player
    elif position == "6":
        board[1][2] = player
    elif position == "7":
        board[2][0] = player
    elif position == "8":
        board[2][1] = player
    elif position == "9":
        board[2][2] = player

    return board

def play():
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]
    instructions(board)
    won = False
    currentplayer = "X"
    while not won:
        player = currentplayer
        move(board, player)
        won = check_win(board, player)
        displayboard(board)
        winner = currentplayer
        if currentplayer == "X":
            currentplayer = "O"
        else:
            currentplayer = "X"
    print(f"The winner is {winner}")
    print("Would you like to play again? Y/N")
    answer = input().upper()
    while answer not in ["Y", "N"]:
        print("You must enter a Y or an N")
        answer = input().upper()
    if answer == "Y":
        play()

play()