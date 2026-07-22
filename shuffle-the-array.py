# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def shuffle(nums, n):
    # Initialize an empty list to store the shuffled array
    shuffled = []
    
    # Loop through the first half of the array
    for i in range(n):
        # Append the current element from the first half
        shuffled.append(nums[i])
        
        # Append the corresponding element from the second half
        shuffled.append(nums[n + i])
    
    # Return the shuffled array
    return shuffled