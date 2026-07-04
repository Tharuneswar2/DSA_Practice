def numWaterBottles(numBottles, numExchange):
    # Initialize the total number of bottles that can be drunk
    total_drunk = numBottles
    
    # Initialize the number of empty bottles
    empty_bottles = numBottles
    
    # Continue the process until we cannot exchange empty bottles for a new one
    while empty_bottles >= numExchange:
        # Calculate the number of new bottles we can get by exchanging empty bottles
        new_bottles = empty_bottles // numExchange
        
        # Update the total number of bottles that can be drunk
        total_drunk += new_bottles
        
        # Update the number of empty bottles
        empty_bottles = new_bottles + (empty_bottles % numExchange)
    
    return total_drunk