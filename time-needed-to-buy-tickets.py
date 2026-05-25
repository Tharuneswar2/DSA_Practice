def timeRequiredToBuy(tickets, k):
    # Initialize the total time
    total_time = 0
    
    # Iterate over the tickets
    for i, ticket in enumerate(tickets):
        # If the current ticket is to the right of the target ticket
        if i <= k:
            # Add the minimum of the current ticket and the target ticket to the total time
            total_time += min(ticket, tickets[k])
        else:
            # Add the minimum of the current ticket and the target ticket minus one to the total time
            total_time += min(ticket, tickets[k] - 1)
    
    # Return the total time
    return total_time