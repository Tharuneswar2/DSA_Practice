def bowling_winner(rolls):
    # Initialize scores and current roll index for both players
    scores = [0, 0]
    current_roll_index = 0

    # Iterate over each roll
    for i in range(len(rolls)):
        # Determine the current player
        player = i % 2

        # Add the current roll to the player's score
        scores[player] += rolls[i]

        # Check for strike
        if rolls[i] == 10:
            # Add the next two rolls to the player's score
            if i < len(rolls) - 2:
                scores[player] += rolls[i + 1] + rolls[i + 2]
            # Skip the next roll
            i += 1

        # Check for spare
        elif i < len(rolls) - 1 and rolls[i] + rolls[i + 1] == 10:
            # Add the next roll to the player's score
            if i < len(rolls) - 2:
                scores[player] += rolls[i + 2]
            # Skip the next roll
            i += 1

    # Return the winner
    if scores[0] > scores[1]:
        return 1
    elif scores[1] > scores[0]:
        return 2
    else:
        return 0  # Tie

# Example usage:
rolls = [10, 9, 1, 5, 5, 7, 2, 10, 10, 9, 0, 8, 2, 9, 1, 9, 1]
print(bowling_winner(rolls))