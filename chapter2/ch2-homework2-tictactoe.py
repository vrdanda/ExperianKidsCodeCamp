def print_board(board):
    for row in board:
        print(" ".join(row))

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    for _ in range(9):
        row, col = map(int, input(f"Player {players[current_player]}, enter row and column (0-2): ").split())
        if board[row][col] == " ":
            board[row][col] = players[current_player]
            print_board(board)
            if check_winner(board, players[current_player]):
                print(f"Player {players[current_player]} wins!")
                break
            current_player = (current_player + 1) % 2
        else:
            print("Cell already occupied. Try again.")

    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()