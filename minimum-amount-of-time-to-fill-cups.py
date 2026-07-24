# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def fillCups(self, amount: List[int]) -> int:
    # Sort the amounts in descending order to prioritize the largest amounts first
    amount.sort(reverse=True)
    
    # Initialize the total time and the index for the current amount
    total_time = 0
    i = 0
    
    # Continue filling cups until all amounts have been processed
    while i < len(amount):
        # If there are at least two amounts left, fill the first two cups
        if i + 1 < len(amount):
            # Fill the first two cups and increment the total time
            total_time += max(amount[i], amount[i+1])
            # Move to the next two amounts
            i += 2
        # If there is only one amount left, fill the last cup
        else:
            # Fill the last cup and increment the total time
            total_time += amount[i]
            # Move to the next amount (which doesn't exist, so the loop will end)
            i += 1
    
    # Return the total time
    return total_time