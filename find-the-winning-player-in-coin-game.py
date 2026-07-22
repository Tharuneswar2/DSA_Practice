# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def find_winner(coins):
    # Calculate the total number of coins
    n = len(coins)
    
    # Initialize a prefix sum array to store the cumulative sum of coins
    prefix_sum = [0] * (n + 1)
    
    # Calculate the prefix sum
    for i in range(n):
        # The prefix sum at index i is the sum of all coins from index 0 to i
        prefix_sum[i + 1] = prefix_sum[i] + coins[i]
    
    # Initialize a 2D array to store the maximum number of coins that can be picked by the current player
    dp = [[0] * n for _ in range(n)]
    
    # Fill the dp array in a bottom-up manner
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            # If the length is 1, the maximum number of coins that can be picked is the coin at the current index
            if length == 1:
                dp[i][j] = coins[i]
            # If the length is 2, the maximum number of coins that can be picked is the maximum of the two coins
            elif length == 2:
                dp[i][j] = max(coins[i], coins[j])
            # If the length is more than 2, the maximum number of coins that can be picked is the maximum of the following two cases:
            # 1. Pick the coin at the current index and the remaining coins that can be picked by the other player
            # 2. Pick the coin at the last index and the remaining coins that can be picked by the other player
            else:
                dp[i][j] = max(prefix_sum[j + 1] - prefix_sum[i] - dp[i + 1][j], prefix_sum[j + 1] - prefix_sum[i] - dp[i][j - 1])
    
    # The maximum number of coins that can be picked by the first player is stored in dp[0][n - 1]
    # If the maximum number of coins that can be picked by the first player is more than the total number of coins divided by 2,
    # the first player wins, otherwise the second player wins
    return "First" if dp[0][n - 1] > prefix_sum[n] / 2 else "Second"