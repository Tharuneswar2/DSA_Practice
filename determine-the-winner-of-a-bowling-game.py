# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def bowling_game_winner(player1, player2):
    # Initialize scores for both players
    score1, score2 = 0, 0
    
    # Iterate over each frame in the game
    for i in range(10):
        # Check if the current frame is a strike for player 1
        if player1[i] == 'X':
            # Add 10 points to the score and add the next two rolls
            score1 += 10 + get_next_two_rolls(player1, i)
        # Check if the current frame is a spare for player 1
        elif player1[i+1] == '/':
            # Add 10 points to the score and add the next roll
            score1 += 10 + get_next_roll(player1, i+2)
        # If it's not a strike or spare, add the points for the current frame
        else:
            score1 += get_frame_points(player1, i)
        
        # Repeat the same process for player 2
        if player2[i] == 'X':
            score2 += 10 + get_next_two_rolls(player2, i)
        elif player2[i+1] == '/':
            score2 += 10 + get_next_roll(player2, i+2)
        else:
            score2 += get_frame_points(player2, i)
    
    # Return the winner based on the scores
    if score1 > score2:
        return 'player1'
    elif score2 > score1:
        return 'player2'
    else:
        return 'tie'

def get_next_two_rolls(player, index):
    # Get the next two rolls after a strike
    if index < 9:
        if player[index+2] == 'X':
            return 10 + get_next_roll(player, index+3)
        elif player[index+3] == '/':
            return 10
        else:
            return get_frame_points(player, index+2)
    else:
        return 0

def get_next_roll(player, index):
    # Get the next roll after a spare
    if index < 10:
        if player[index] == 'X':
            return 10
        else:
            return int(player[index])
    else:
        return 0

def get_frame_points(player, index):
    # Calculate the points for a regular frame
    if player[index] == 'X':
        return 10
    elif player[index+1] == '/':
        return 10
    else:
        return int(player[index]) + int(player[index+1])