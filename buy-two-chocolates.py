# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def buy_two_chocolates(candies, wrapper_cost, candy_cost):
    # Calculate the total number of candies that can be bought with the given amount of money
    total_candies = candies // candy_cost
    
    # Initialize the total number of wrappers
    total_wrappers = total_candies
    
    # Continue the process until we have enough wrappers to buy more candies
    while total_wrappers >= wrapper_cost:
        # Calculate the number of new candies that can be bought with the current wrappers
        new_candies = total_wrappers // wrapper_cost
        
        # Update the total number of candies and wrappers
        total_candies += new_candies
        total_wrappers = new_candies + (total_wrappers % wrapper_cost)
    
    # Return the total number of candies
    return total_candies