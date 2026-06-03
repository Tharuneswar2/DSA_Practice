def min_cuts_to_divide_circle(n):
    # If the number of cuts is less than 2, we can't divide the circle
    if n < 2:
        return 0
    
    # Initialize a list to store the minimum cuts for each number of cuts
    dp = [0] * (n + 1)
    
    # For 2 cuts, we can divide the circle into 2 parts
    dp[2] = 1
    
    # For 3 cuts, we can divide the circle into 3 parts
    dp[3] = 2
    
    # For more than 3 cuts, we can divide the circle into more parts
    for i in range(4, n + 1):
        # Initialize the minimum cuts for the current number of cuts
        min_cuts = i - 1
        
        # Try all possible previous cuts
        for j in range(2, i):
            # Update the minimum cuts if we can divide the circle into more parts
            min_cuts = min(min_cuts, dp[j] + dp[i - j] + 1)
        
        # Store the minimum cuts for the current number of cuts
        dp[i] = min_cuts
    
    # Return the minimum cuts for the given number of cuts
    return dp[n]

print(min_cuts_to_divide_circle(4))  # Output: 3
print(min_cuts_to_divide_circle(6))  # Output: 4