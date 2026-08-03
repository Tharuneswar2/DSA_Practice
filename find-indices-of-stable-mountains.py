# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def findStableMountains(heights):
    # Initialize an empty list to store the indices of stable mountains
    stable_mountains = []
    
    # Iterate over the list of heights
    for i in range(len(heights)):
        # Check if the current height is greater than its neighbors
        if (i == 0 or heights[i] > heights[i-1]) and (i == len(heights)-1 or heights[i] > heights[i+1]):
            # If the current height is greater than its neighbors, add its index to the list of stable mountains
            stable_mountains.append(i)
    
    # Return the list of indices of stable mountains
    return stable_mountains