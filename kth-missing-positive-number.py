def findKthPositive(arr, k):
    # Initialize a set with the given array for efficient lookups
    num_set = set(arr)
    
    # Initialize a counter for the missing numbers
    missing_count = 0
    
    # Initialize a counter for the current number
    current_num = 1
    
    # Loop until we find the kth missing number
    while True:
        # If the current number is not in the set, it's a missing number
        if current_num not in num_set:
            # Increment the missing number counter
            missing_count += 1
            
            # If this is the kth missing number, return it
            if missing_count == k:
                return current_num
        
        # Move on to the next number
        current_num += 1