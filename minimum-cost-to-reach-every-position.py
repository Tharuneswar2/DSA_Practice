# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def minCostToReachEveryPosition(costs):
    # Initialize the number of houses and colors
    n = len(costs)
    k = len(costs[0])
    
    # Create a 2D array to store the minimum cost for each house and color
    dp = [[0] * k for _ in range(n)]
    
    # Initialize the minimum cost for the first house
    dp[0] = costs[0]
    
    # Iterate over each house starting from the second house
    for i in range(1, n):
        # Initialize the minimum cost for the current house and color
        min_cost = float('inf')
        second_min_cost = float('inf')
        min_color = -1
        second_min_color = -1
        
        # Find the minimum and second minimum cost for the previous house
        for j in range(k):
            if dp[i-1][j] < min_cost:
                second_min_cost = min_cost
                second_min_color = min_color
                min_cost = dp[i-1][j]
                min_color = j
            elif dp[i-1][j] < second_min_cost:
                second_min_cost = dp[i-1][j]
                second_min_color = j
        
        # Update the minimum cost for the current house and color
        for j in range(k):
            if j != min_color:
                dp[i][j] = min_cost + costs[i][j]
            else:
                dp[i][j] = second_min_cost + costs[i][j]
    
    # Return the minimum cost for the last house
    return min(dp[-1])