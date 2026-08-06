# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def kidsWithCandies(candies, extraCandies):
    # Find the maximum number of candies any kid has
    max_candies = max(candies)
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the number of candies each kid has
    for candy in candies:
        # Check if the kid can have the greatest number of candies by adding extraCandies
        # If the kid's candies plus extraCandies is greater than or equal to the max_candies, append True to the result
        # Otherwise, append False
        result.append(candy + extraCandies >= max_candies)
    
    # Return the result
    return result