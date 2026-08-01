# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def maxEnemyForts(n, forts):
    # Initialize variables to store the maximum number of enemy forts that can be captured
    # and the current number of enemy forts that can be captured
    max_forts = 0
    curr_forts = 0
    
    # Initialize variables to store the previous and current fort types
    prev_fort = 0
    curr_fort = 0
    
    # Iterate over the forts
    for i in range(n):
        # If the current fort is an enemy fort
        if forts[i] == 1:
            # If the previous fort is not an enemy fort, increment the current number of enemy forts
            if prev_fort == 0:
                curr_forts += 1
            # Update the maximum number of enemy forts if the current number is greater
            max_forts = max(max_forts, curr_forts)
        else:
            # If the current fort is not an enemy fort, reset the current number of enemy forts
            curr_forts = 0
        
        # Update the previous fort type
        prev_fort = forts[i]
    
    # Return the maximum number of enemy forts that can be captured
    return max_forts