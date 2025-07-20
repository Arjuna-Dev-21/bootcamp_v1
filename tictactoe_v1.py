def display_board(board):
    print("\nTIC TAC TOE")
    print("*****************")
    for i in range(3):
        # Row with content (X/O)
        print(f"*  {board[i][0]}  | {board[i][1]} |  {board[i][2]}  *")
        if i < 2:
            # Separator between rows
            print("*  ---|---|---  *")
    print("*****************\n")


def player_input(player):
    while True:
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            if row not in range(3) or col not in range(3):
                print("Invalid row or column. Use numbers from 1 to 3.")
            else:
                return row, col
        except ValueError:
            print("Please enter valid numbers.")


def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_full(board):
    return all(cell in ["X", "O"] for row in board for cell in row)


def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    print("Welcome to TIC TAC TOE!")

    while True:
        display_board(board)
        print(f"Player {current_player}'s turn...")
        row, col = player_input(current_player)

        if board[row][col] != " ":
            print("That cell is already taken. Try again.")
            continue

        board[row][col] = current_player

        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins! 🎉")
            break

        if is_full(board):
            display_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"


# Start the game
if __name__ == "__main__":
    play()
