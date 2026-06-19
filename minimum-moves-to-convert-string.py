def minimumMoves(s: str) -> int:
    # Initialize the count of moves and the index of the current character
    moves = 0
    i = 0
    
    # Iterate over the string
    while i < len(s):
        # If the current character is 'X', we need to make a move
        if s[i] == 'X':
            # Increment the moves count
            moves += 1
            
            # We can skip the next two characters because they will be 'O's
            i += 3
        else:
            # If the current character is 'O', we don't need to make a move
            i += 1
    
    # Return the total moves
    return moves