def score_of_string(s):
    # Initialize the score and the multiplier
    score = 0
    multiplier = 1
    
    # Iterate over the string from right to left
    for i in range(len(s) - 1, -1, -1):
        # If the character is 'L', add the multiplier to the score
        if s[i] == 'L':
            score += multiplier
        # If the character is 'R', double the multiplier
        elif s[i] == 'R':
            multiplier *= 2
    
    # Return the score
    return score