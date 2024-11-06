# Text version based of Tic Tac Toe game in Python

# Initialize the board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    print("\n")
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")
    print("\n")

# Function to check for a winner
def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full
def check_draw():
    return " " not in board

# Function to make a move
def make_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move >= 0 and move < 9 and board[move] == " ":
                board[move] = player
                break
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

# Main game loop
def play_game():
    current_player = "X"
    while True:
        print_board()
        make_move(current_player)
        
        # Check for win or draw
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        elif check_draw():
            print_board()
            print("It's a draw!")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()
