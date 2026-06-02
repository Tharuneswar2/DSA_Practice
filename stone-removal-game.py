def stoneGame(piles):
    n = len(piles)
    dp = [[0]*n for _ in range(n)]
    
    # Initialize dp table with base case where only one pile is left
    for i in range(n):
        dp[i][i] = piles[i]
        
    # Fill dp table in a bottom-up manner
    for d in range(1, n):
        for i in range(n-d):
            j = i + d
            # If it's Alex's turn, he will try to maximize his score
            # He can either pick the first pile or the last pile
            # The opponent will try to minimize Alex's score
            dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
            
    # If Alex's score is greater than 0, he will win the game
    return dp[0][n-1] > 0

# Test the function
piles = [5,3,4,5]
print(stoneGame(piles))  # Output: True