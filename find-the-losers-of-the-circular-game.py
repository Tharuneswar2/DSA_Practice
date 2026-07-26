# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def circularGameLosers(self, n: int, k: int) -> List[int]:
    # Initialize a set to store the losers
    losers = set()
    
    # Initialize the current marble position
    marble = 1
    
    # Initialize the current player
    player = 0
    
    # Continue the game until all players have lost
    while len(losers) < n - 1:
        # If the current player has already lost, skip their turn
        if player in losers:
            player = (player + 1) % n
            continue
        
        # Calculate the next marble position
        marble = (marble + k - 1) % n + 1
        
        # If the next marble position is 1, the current player loses
        if marble == 1:
            losers.add(player)
        
        # Move to the next player
        player = (player + 1) % n
    
    # The remaining players are the losers
    losers = [i for i in range(n) if i not in losers]
    
    # Return the losers in ascending order
    return sorted(losers)