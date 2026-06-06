def circularGameLosers(n, k):
    # Initialize a set to store the losers
    losers = set()
    
    # Initialize the current position and the number of moves
    i, moves = 1, 0
    
    # Continue the game until we reach the starting position again
    while True:
        # If the current position is already in the losers set, we've reached the starting position again
        if i in losers:
            break
        
        # Add the current position to the losers set
        losers.add(i)
        
        # Calculate the next position
        i = (i + k - 1) % n + 1
        
        # Increment the number of moves
        moves += 1
        
        # If the number of moves is equal to n, we've reached the starting position again
        if moves == n:
            break
    
    # Convert the losers set to a list and sort it
    losers = sorted(list(losers))
    
    # Return the losers
    return losers