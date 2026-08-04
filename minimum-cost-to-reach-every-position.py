# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def minCostToReachEveryPosition(cost):
    # Get the number of positions
    n = len(cost)
    
    # Initialize a list to store the minimum cost to reach each position
    min_cost = [0] * n
    
    # The minimum cost to reach the first position is the cost of the first position itself
    min_cost[0] = cost[0]
    
    # Calculate the minimum cost to reach each position from the second position to the end
    for i in range(1, n):
        # Initialize the minimum cost to reach the current position as infinity
        min_cost[i] = float('inf')
        
        # Check all previous positions to find the one that results in the minimum cost
        for j in range(i):
            # If the current position is reachable from the previous position
            if i - j <= 2:
                # Update the minimum cost to reach the current position
                min_cost[i] = min(min_cost[i], min_cost[j] + cost[i])
    
    # Return the minimum cost to reach every position
    return min_cost

def minCostToReachEveryPositionOptimized(cost):
    # Get the number of positions
    n = len(cost)
    
    # Initialize a list to store the minimum cost to reach each position
    min_cost = [0] * n
    
    # The minimum cost to reach the first position is the cost of the first position itself
    min_cost[0] = cost[0]
    
    # Initialize variables to store the minimum cost to reach the previous two positions
    prev_prev_cost = cost[0]
    prev_cost = cost[0]
    
    # Calculate the minimum cost to reach each position from the second position to the end
    for i in range(1, n):
        # If this is the second position, update the minimum cost and the previous cost
        if i == 1:
            min_cost[i] = cost[0] + cost[1]
            prev_cost = min_cost[i]
        # If this is the third position, update the minimum cost and the previous two costs
        elif i == 2:
            min_cost[i] = min(cost[0] + cost[2], cost[1] + cost[2])
            prev_prev_cost = prev_cost
            prev_cost = min_cost[i]
        # For other positions, update the minimum cost and the previous two costs
        else:
            min_cost[i] = min(prev_prev_cost, prev_cost) + cost[i]
            prev_prev_cost = prev_cost
            prev_cost = min_cost[i]
    
    # Return the minimum cost to reach every position
    return min_cost