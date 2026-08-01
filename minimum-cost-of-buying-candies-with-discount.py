# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def minCost(candies, coins, extraCandies):
    # Sort the candies array in ascending order to easily find the minimum cost
    candies.sort()
    
    # Initialize the minimum cost as infinity
    min_cost = float('inf')
    
    # Iterate over each candy in the sorted candies array
    for candy in candies:
        # Calculate the cost of buying the current candy with the given coins and extra candies
        cost = max(0, candy - coins - extraCandies)
        
        # Update the minimum cost if the current cost is less than the minimum cost
        min_cost = min(min_cost, cost)
    
    # Return the minimum cost
    return min_cost