def minCost(logs, a, b):
    # Initialize the total cost to 0
    total_cost = 0
    
    # Sort the logs in ascending order
    logs.sort()
    
    # Initialize two pointers, one at the start and one at the end of the logs
    i, j = 0, len(logs) - 1
    
    # Continue the process until the two pointers meet
    while i < j:
        # Calculate the cost of transporting the current logs
        cost = min(a * (logs[j] - logs[i]), b * (j - i + 1))
        
        # Add the cost to the total cost
        total_cost += cost
        
        # Move the pointers based on the cost
        if a * (logs[j] - logs[i]) < b * (j - i + 1):
            j -= 1
        else:
            i += 1
    
    # Return the total cost
    return total_cost

# Test the function
logs = [1, 2, 3, 4, 5]
a = 2
b = 3
print(minCost(logs, a, b))