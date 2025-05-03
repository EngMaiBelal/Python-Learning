# Tic-Tac-Toe game
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if all(s == player for s in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)):
        return True
    
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_draw(board):
    # If all cells are filled and there's no winner, it's a draw
    for row in board:
        if ' ' in row:
            return False
    return True

def tic_tac_toe():
    # Initialize the board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'  # Player 1 starts as 'X'
    
    print("Welcome to Tic-Tac-Toe!")
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        # Get valid input for row and column
        try:
            row, col = map(int, input("Enter row and column (0, 1, 2) separated by space: ").split())
            if board[row][col] != ' ':
                print("Cell already occupied, try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column numbers between 0 and 2.")
            continue
        
        # Place the player's mark
        board[row][col] = current_player
        
        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch to the next player
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
tic_tac_toe()
