# Initialize the board with numbers showing positions (1-9)
board = [str(i+1) for i in range(9)]

# Function to print the current state of the board
def print_board():
    # Print the board in a 3x3 grid format
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Function to take the player's move
def player_move(symbol):
    # Ask the player for their move and adjust it to 0-based index
    move = int(input(f"Enter your move for {symbol} (1-9): ")) - 1
    # If the chosen spot is not already taken by X or O, assign it to the player
    if board[move] not in ['X', 'O']:
        board[move] = symbol
    else:
        # If the spot is taken, ask the player to try again
        print("Invalid move, try again.")
        player_move(symbol)

# Function to check if a player has won
def check_winner(symbol):
    # All possible winning combinations
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # columns
        (0, 4, 8), (2, 4, 6)             # diagonals
    ]
    # Check if any winning condition is met by the current player
    return any(all(board[i] == symbol for i in condition) for condition in win_conditions)

# Main game function
def game():
    # Loop for 9 turns (maximum moves in a Tic-Tac-Toe game)
    for turn in range(9):
        # Print the current board state
        print_board()
        # Alternating players: X for even turns, O for odd turns
        symbol = 'X' if turn % 2 == 0 else 'O'
        # Player makes a move
        player_move(symbol)
        # Check if the current player has won
        if check_winner(symbol):
            print_board()  # Print the final board
            print(f"Player {symbol} wins!")  # Announce the winner
            return  # End the game
    # If no winner after 9 turns, it's a tie
    print_board()
    print("It's a tie!")

# Start the game
game()
