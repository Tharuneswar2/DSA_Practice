def findWinners(matches):
    # Create a dictionary to store the number of losses for each player
    losses = {}
    
    # Iterate over each match
    for winner, loser in matches:
        # Increment the loss count for the loser
        losses[loser] = losses.get(loser, 0) + 1
        # Ensure the winner is in the dictionary with 0 losses
        losses[winner] = losses.get(winner, 0)
    
    # Initialize lists to store players with 0 and 1 loss
    zero_losses = []
    one_loss = []
    
    # Iterate over the losses dictionary
    for player, loss in losses.items():
        # If the player has 0 losses, add them to the zero_losses list
        if loss == 0:
            zero_losses.append(player)
        # If the player has 1 loss, add them to the one_loss list
        elif loss == 1:
            one_loss.append(player)
    
    # Return the number of players with 0 and 1 loss
    return [zero_losses, one_loss]

# Example usage:
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(findWinners(matches))