def minCost(candies):
    # Sort the candies in descending order
    candies.sort(reverse=True)
    
    # Initialize the total cost and the number of candies to buy
    total_cost = 0
    num_to_buy = len(candies)
    
    # Iterate over the sorted candies
    for i in range(num_to_buy):
        # If the index is a multiple of 3, it's free
        if (i + 1) % 3 == 0:
            continue
        # Add the cost of the candy to the total cost
        total_cost += candies[i]
    
    return total_cost