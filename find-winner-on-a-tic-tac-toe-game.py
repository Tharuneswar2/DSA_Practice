# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def find_winner(board):
    # Check rows for a winner
    for row in board:
        # If all elements in the row are the same and not empty, return the winner
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    # Check columns for a winner
    for col in range(3):
        # If all elements in the column are the same and not empty, return the winner
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # Check diagonals for a winner
    # If all elements in the main diagonal are the same and not empty, return the winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    # If all elements in the other diagonal are the same and not empty, return the winner
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    # If no winner is found, return None
    return None

# Example usage:
board = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['O', 'X', 'X']
]
print(find_winner(board))  # Output: X