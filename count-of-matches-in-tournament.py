# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def numberOfMatches(n: int) -> int:
    # Initialize a variable to store the total number of matches
    total_matches = 0
    
    # In a tournament, the number of matches is equal to the number of teams minus one
    # This is because each match eliminates one team, and the tournament continues until only one team is left
    # So, we can calculate the total number of matches by subtracting one from the number of teams
    # However, this approach does not take into account the number of matches in each round
    # A more efficient approach is to use the formula: total_matches = n - 1
    
    # But we can also solve this problem using a while loop
    # We start with the number of teams and keep dividing it by 2 until we have only one team left
    # In each iteration, we add the number of matches in the current round to the total number of matches
    # The number of matches in each round is equal to the number of teams divided by 2
    # We use integer division (//) to get the number of matches in each round
    while n > 1:
        # Calculate the number of matches in the current round
        matches_in_round = n // 2
        
        # Add the number of matches in the current round to the total number of matches
        total_matches += matches_in_round
        
        # Update the number of teams for the next round
        n = matches_in_round
    
    # Return the total number of matches
    return total_matches