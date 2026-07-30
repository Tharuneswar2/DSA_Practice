# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def applyOperations(nums):
    # Initialize an empty list to store the result
    result = []
    
    # Initialize a variable to keep track of the number of zeros encountered
    zeros = 0
    
    # Iterate over the input list
    for num in nums:
        # If the current number is zero, increment the zeros counter
        if num == 0:
            zeros += 1
        # If the current number is not zero, append it to the result list
        else:
            # If zeros have been encountered before this number, append zeros to the result list first
            if zeros > 0:
                result.extend([0] * zeros)
                # Reset the zeros counter
                zeros = 0
            # Append the current number to the result list
            result.append(num)
    
    # If there are any remaining zeros, append them to the end of the result list
    if zeros > 0:
        result.extend([0] * zeros)
    
    # Return the result list
    return result