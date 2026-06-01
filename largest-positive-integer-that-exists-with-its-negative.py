def findMaxK(nums):
    # Create a set from the list for efficient lookups
    num_set = set(nums)
    
    # Initialize max_k to a negative value
    max_k = -1
    
    # Iterate over the set
    for num in num_set:
        # Check if the negative of the current number exists in the set
        if -num in num_set:
            # Update max_k if the current number is greater
            max_k = max(max_k, num)
    
    # Return max_k if it's positive, otherwise return -1
    return max_k if max_k > 0 else -1