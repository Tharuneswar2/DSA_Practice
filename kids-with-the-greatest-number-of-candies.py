def kidsWithCandies(candies, extraCandies):
    # Find the maximum number of candies any kid has
    max_candies = max(candies)
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the number of candies each kid has
    for candy in candies:
        # Check if the kid can have the greatest number of candies after receiving extraCandies
        if candy + extraCandies >= max_candies:
            # If true, append True to the result list
            result.append(True)
        else:
            # If false, append False to the result list
            result.append(False)
    
    # Return the result list
    return result