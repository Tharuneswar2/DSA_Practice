def maxScore(s):
    # Initialize variables to store the maximum score and the current score
    max_score = 0
    current_score = 0
    
    # Initialize variables to store the count of 1s and 0s
    ones = 0
    zeros = 0
    
    # Count the total number of 1s in the string
    for char in s:
        if char == '1':
            ones += 1
    
    # Iterate over the string from left to right
    for i in range(len(s) - 1):
        # If the current character is '0', increment the zeros count
        if s[i] == '0':
            zeros += 1
        # If the current character is '1', decrement the ones count
        else:
            ones -= 1
        
        # Update the current score
        current_score = zeros + ones
        
        # Update the maximum score if the current score is higher
        max_score = max(max_score, current_score)
    
    # Return the maximum score
    return max_score