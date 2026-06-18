def canWin(n):
    # If the number of coins is less than 5, the first player can always win
    if n < 5:
        return True
    
    # Initialize a list to store the results of subproblems
    dp = [False] * (n + 1)
    
    # Base cases
    dp[1] = dp[2] = dp[3] = dp[4] = True
    
    # Fill up the dp table
    for i in range(5, n + 1):
        # If the current player can't win in the previous 4 moves, 
        # then the current player can win
        dp[i] = not (dp[i - 1] and dp[i - 2] and dp[i - 3] and dp[i - 4])
    
    # Return the result
    return dp[n]

def findWinner(n):
    # If the first player can win, return 1
    if canWin(n):
        return 1
    # Otherwise, return 2
    else:
        return 2

# Test the function
print(findWinner(5))  # Output: 1
print(findWinner(6))  # Output: 2