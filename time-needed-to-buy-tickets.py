# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def timeRequiredToBuy(tickets, k):
    # Initialize the total time to 0
    total_time = 0
    
    # Iterate over the tickets array
    for i, ticket in enumerate(tickets):
        # If the current ticket is to the right of the target ticket (k), 
        # we only need to consider the minimum of the current ticket and the remaining tickets of the target ticket
        if i <= k:
            # Add the minimum of the current ticket and the remaining tickets of the target ticket to the total time
            total_time += min(ticket, tickets[k] - (k - i))
        else:
            # If the current ticket is to the left of the target ticket (k), 
            # we only need to consider the minimum of the current ticket and the remaining tickets of the target ticket
            # But we don't need to subtract (k - i) because we are already to the right of the target ticket
            total_time += min(ticket, tickets[k])
    
    # Return the total time
    return total_time