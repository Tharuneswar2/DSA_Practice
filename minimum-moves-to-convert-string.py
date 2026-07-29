# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def minimumMoves(s: str) -> int:
    # Initialize the count of moves and the index of the current character
    moves = 0
    i = 0
    
    # Loop through the string
    while i < len(s):
        # If the current character is 'X', increment the moves and skip the next two characters
        if s[i] == 'X':
            moves += 1
            # Skip the next two characters
            i += 3
        else:
            # If the current character is not 'X', move to the next character
            i += 1
    
    # Return the total moves
    return moves