# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def distributeCandies(candies, num_people):
    # Initialize the candies given to each person as 0
    candies_given = [0] * num_people
    
    # Initialize the index of the current person
    i = 0
    
    # Continue distributing candies until there are no more candies left
    while candies > 0:
        # Calculate the number of candies to give to the current person
        # This is the minimum of the number of candies left and the index of the current person plus 1
        # This ensures that we don't give more candies than we have left
        candies_to_give = min(candies, i + 1)
        
        # Give the calculated number of candies to the current person
        candies_given[i] += candies_to_give
        
        # Subtract the number of candies given from the total number of candies
        candies -= candies_to_give
        
        # Move to the next person
        i = (i + 1) % num_people
    
    # Return the list of candies given to each person
    return candies_given