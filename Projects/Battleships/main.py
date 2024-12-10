board_template = [
    [" ", "A", "B", "C", "D", "E", "F", "G", "H"],
    ["1", " ", " ", " ", " ", " ", " ", " ", " "],
    ["2", " ", " ", " ", " ", " ", " ", " ", " "],
    ["3", " ", " ", " ", " ", " ", " ", " ", " "],
    ["4", " ", " ", " ", " ", " ", " ", " ", " "],
    ["5", " ", " ", " ", " ", " ", " ", " ", " "],
    ["6", " ", " ", " ", " ", " ", " ", " ", " "],
    ["7", " ", " ", " ", " ", " ", " ", " ", " "],
    ["8", " ", " ", " ", " ", " ", " ", " ", " "]
]

mappings = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8
}

from getpass import getpass as prompt
import os

# prompt(prompt="Press any key to continue...")

def clear():
    os.system("cls")

player_1_board = board_template
player_1_guesses = board_template
player_2_board = board_template
player_2_guesses = board_template

player_turn = 1

def display_board(board):
    for row in board:
        print(row)

def fill_board(player: int, locations: list):
    for coordinates in locations:
        coord: list = list(coordinates)
        coord[0] = int(mappings[coord[0]])
        coord[1] = int(coord[1])
        coord.reverse()
        
        match player:
            case 1:
                player_1_board[coord[0]][coord[1]] = "\u26F5" # ship
            case 2:
                player_2_board[coord[0]][coord[1]] = "\u26F5" # ship

def hit_detect(player: int, location: str):
    global player_turn

    location: list = list(location)
    
    location[0] = int(mappings[location[0]])
    location[1] = int(location[1])

    location.reverse()

    if player == 1:
        guess_location = player_2_board[location[0]][location[1]]
        if guess_location == "\u26F5": # if the guess was a ship
            player_1_guesses[location[0]][location[1]] = "\U0001F4A5" # explosion symbol
            player_turn = 2
        elif guess_location == " ":
            player_1_guesses[location[0]][location[1]] = "\U0001F30A" # water symbol
            player_turn = 2
        else:
            player_turn = 1
        display_board(player_1_guesses)
    elif player == 2:
        ...

def initialise_player(player: int):
    initialised = False
    display_board(board_template)
    while not initialised:
        try:
            
            locations = input("Please enter 5 coordinates that you'd like to place your boats. These MUST be separated by commas (Accepted formats: A-3, B 6, C8)\nCoordinates: ").upper().replace("-", "").replace(" ", "").split(",")
            for coord in locations:
                if (len(coord) == 2) and (coord[0] in ("ABCDEFGH")) and (str(coord[1]) in "12345678"):
                    pass
                else:
                    raise LookupError
            if len(set(locations)) == 5:
                fill_board(player, locations)
                display_board(player_1_board if player == 1 else player_2_board)
                initialised = True
            else:
                raise ValueError
        except ValueError:
            print("ERROR: Please input *5* unique coordinates!")
        except TypeError:
            print("ERROR: Please input 5 UNIQUE coordinates!")
        except LookupError:
            print("ERROR: Your coordinates must be formatted as Row-Column (Accepted formats: A-3, B 6, C8). Rows being (A-H), Columns being (1-8)")
        except (EOFError, KeyboardInterrupt):
            pass

if __name__ == "__main__":
    # hit_detect(player=1, location="C5")
    # display_board(player_1_guesses)
    
    # fill_board(1, input("Coords: ").replace(" ", "").split(","))
    # display_board(player_1_board)

    ##### ACTUAL GAME #####
    try:
        initialise_player(player=1)
        prompt(prompt="Player 1: Press ENTER to hide your board so that player 2 can set theirs")
        clear()
        initialise_player(player=2)
        while True:
            try:
                prompt(prompt="Player 2: Press ENTER to hide your board")
                clear()
                match player_turn:
                    case 1:
                        user_guess = input("Guess coords: ")
                        hit_detect(1, user_guess)
                    case 2:
                        user_guess = input("Guess coords: ")
                        hit_detect(2, user_guess)
            except:
                ...
    except (EOFError, KeyboardInterrupt):
        print("STOP TRYING TO RUIN THE GAME BY CRASHING IT")

# Example (for testing):
# A1, B2, C3, H5, D4