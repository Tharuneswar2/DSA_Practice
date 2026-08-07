# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def findWinners(matches):
    # Create a dictionary to store the number of losses for each player
    losses = {}
    
    # Iterate over each match
    for winner, loser in matches:
        # If the winner is not in the dictionary, add it with 0 losses
        if winner not in losses:
            losses[winner] = 0
        # If the loser is not in the dictionary, add it with 1 loss
        if loser not in losses:
            losses[loser] = 1
        # If the loser is already in the dictionary, increment its losses by 1
        else:
            losses[loser] += 1
    
    # Initialize lists to store players with 0 and 1 losses
    zero_losses = []
    one_loss = []
    
    # Iterate over the losses dictionary
    for player, loss in losses.items():
        # If a player has 0 losses, add it to the zero_losses list
        if loss == 0:
            zero_losses.append(player)
        # If a player has 1 loss, add it to the one_loss list
        elif loss == 1:
            one_loss.append(player)
    
    # Return the number of players with 0 and 1 losses
    return [len(zero_losses), len(one_loss)]