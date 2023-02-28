game_data = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

game_demo = f"""
                Tik-Tac-Toe
Rules: Kind use the numbers in the demo to tick a box
            (0 0) | (0 1) | (0 2)
            --------------------
            (1 0) | (1 1) | (1 2)
            -------------------- 
            (2 0) | (2 1) | (2 2)
"""


def check_if_box_empty():
    """Checks if all boxes are empty and return True"""
    is_empty = True
    for row in game_data:
        if " " in row:
            is_empty = True
        elif " " not in row:
            is_empty = False

    if not is_empty:
        print("Its a Draw")
    return is_empty


def print_table():
    print(f"     {game_data[0][0]} |  {game_data[0][1]}  | {game_data[0][2]}")
    print(f"    --------------")
    print(f"     {game_data[1][0]} |  {game_data[1][1]}  | {game_data[1][2]}")
    print(f"    --------------")
    print(f"     {game_data[2][0]} |  {game_data[2][1]}  | {game_data[2][2]}")


def check_for_winner():
    "Returns Result of the game"
    winning = False
    winner = None

    # Check rows
    for row in range(3):
        if game_data[row][0] == game_data[row][1] and game_data[row][0] == game_data[row][2] \
                and game_data[row][0] != " ":
            winning, winner = True, game_data[row][0]

    # Check Columns
    for col in range(3):
        if game_data[col][0] != " " and game_data[col][0] == game_data[1][col] \
                and game_data[col][0] == game_data[2][col]:
            winning, winner = True, game_data[col][0]
    # Check diagonal
    if game_data[0][0] != " " and game_data[0][0] == game_data[1][1] and game_data[0][0] == game_data[2][2]:
        winning, winner = True, game_data[0][0]
    elif game_data[0][2] != " " and game_data[0][2] == game_data[1][1] and game_data[col][0] == game_data[2][0]:
        winning, winner = True, game_data[0][2]

    if winning:
        if winner == "X":
            print("Player 1 Wins")
        else:
            print("Player 2 Wins")
    return winning


def play_game(plyer: int):
    """Takes the player and ask the player to play, Return False if players input wrong input else Return True"""
    try:
        player_input = list(map(int, input(f'Player {plyer + 1} turn: ').strip().split()))
        if game_data[player_input[0]][player_input[1]] == " " and plyer + 1 == 1:
            game_data[player_input[0]][player_input[1]] = "X"
        elif game_data[player_input[0]][player_input[1]] == " " and plyer + 1 == 2:
            game_data[player_input[0]][player_input[1]] = "O"
        elif game_data[player_input[0]][player_input[1]] == "X" or game_data[player_input[0]][player_input[1]] == "O":
            print("Position Already Chosen")
    except IndexError:
        print("Opps...Kindly check the demo to know how to tick a box")
        return False
    except ValueError:
        print("Opps...Alphabet are not allowed")
    else:
        return True


print(game_demo)
player = 0
while check_if_box_empty():
    while not play_game(player):
        play_game(player)
    print_table()
    player = (player + 1) % 2
    if check_for_winner():
        break
