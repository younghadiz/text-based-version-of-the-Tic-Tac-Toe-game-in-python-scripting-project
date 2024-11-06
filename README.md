# text-based-version-of-the-Tic-Tac-Toe-game-in-python-scripting-project
The text based version of the Tic Tac Toe game allows two players to take turns placing "X" or "O" on a 3x3 board and then checks for the conditions of the winner in the algorithm after each move and then ends the process when there is a winner or a draw.

# How it Works 
Board Initialization: A list <div style='background-color:gray'>board</div> of 9 spaces represents the 3x3 Tic Tac Toe board.

Printing the Board: print_board() formats and displays the board.

Winning and Draw Conditions: check_winner() checks if the current player has won, and check_draw() checks if the board is full.

Player Moves: make_move() prompts the current player for a move and validates it.

Game Loop: In play_game(), players take turns until there's a winner or a draw.

Each cell on the board is numbered from 1 to 9 for easier input. The game alternates players after each valid move, checking for a winner or a draw after each turn.
