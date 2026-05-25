def distributeCandies(candies, num_people):
    # Initialize an array to store the number of candies each person gets
    distribution = [0] * num_people
    
    # Initialize the index of the current person and the number of candies given
    index, given = 0, 0
    
    # Continue distributing candies until all candies are given
    while given < candies:
        # Calculate the number of candies the current person gets
        # This is the minimum of the remaining candies and the current index plus one
        distribution[index] += min(candies - given, index + 1)
        
        # Update the number of candies given and the index of the current person
        given += index + 1
        index = (index + 1) % num_people
    
    return distribution