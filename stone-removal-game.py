# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def stoneGame(piles):
    # Initialize a 2D array to store the maximum stones that can be collected for each subproblem
    n = len(piles)
    dp = [[0]*n for _ in range(n)]
    
    # Fill the diagonal of the 2D array with the values of the piles
    # This represents the base case where there is only one pile
    for i in range(n):
        dp[i][i] = piles[i]
    
    # Fill the rest of the 2D array in a bottom-up manner
    for d in range(1, n):
        for i in range(n-d):
            j = i + d
            # Calculate the maximum stones that can be collected for the current subproblem
            # This is done by considering two cases: picking the first pile or the last pile
            dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
    
    # The maximum stones that can be collected is stored in the top-right corner of the 2D array
    return dp[0][n-1] > 0