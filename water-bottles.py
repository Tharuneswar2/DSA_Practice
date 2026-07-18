# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def numWaterBottles(numBottles, numExchange):
    # Initialize the total number of bottles that can be drunk
    total_drunk = numBottles
    
    # Initialize the remaining empty bottles
    remaining_empty = numBottles
    
    # Continue the process until there are not enough empty bottles to exchange
    while remaining_empty >= numExchange:
        # Calculate the number of new bottles that can be obtained by exchanging the empty bottles
        new_bottles = remaining_empty // numExchange
        
        # Update the total number of bottles that can be drunk
        total_drunk += new_bottles
        
        # Update the remaining empty bottles
        remaining_empty = new_bottles + (remaining_empty % numExchange)
    
    # Return the total number of bottles that can be drunk
    return total_drunk