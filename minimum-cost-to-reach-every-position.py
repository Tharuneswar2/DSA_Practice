# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def minCostToReachEveryPosition(costs):
    # Initialize a list to store the minimum cost to reach each position
    min_costs = [0] * len(costs)
    
    # The minimum cost to reach the first position is the cost of the first position itself
    min_costs[0] = costs[0]
    
    # Calculate the minimum cost to reach each position from the second position to the end
    for i in range(1, len(costs)):
        # For each position, the minimum cost to reach it is the minimum cost to reach the previous position plus the cost of the current position
        min_costs[i] = min_costs[i-1] + costs[i]
        
    # Return the minimum cost to reach every position
    return min_costs

def minCostToReachEveryPositionOptimized(costs):
    # Initialize variables to store the minimum cost to reach the previous two positions
    prev_prev_cost = costs[0]
    prev_cost = costs[1]
    
    # Initialize a list to store the minimum cost to reach each position
    min_costs = [0] * len(costs)
    
    # The minimum cost to reach the first position is the cost of the first position itself
    min_costs[0] = costs[0]
    
    # The minimum cost to reach the second position is the cost of the second position itself
    min_costs[1] = costs[1]
    
    # Calculate the minimum cost to reach each position from the third position to the end
    for i in range(2, len(costs)):
        # For each position, the minimum cost to reach it is the minimum cost to reach the previous two positions plus the cost of the current position
        min_costs[i] = min(prev_prev_cost, prev_cost) + costs[i]
        
        # Update the minimum cost to reach the previous two positions
        prev_prev_cost = prev_cost
        prev_cost = min_costs[i]
        
    # Return the minimum cost to reach every position
    return min_costs