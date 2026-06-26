def arithmeticTriplets(nums, diff):
    # Create a set of the numbers for efficient lookups
    num_set = set(nums)
    
    # Initialize count of triplets
    count = 0
    
    # Iterate over each number in the list
    for num in nums:
        # Check if the next two numbers in the sequence are in the set
        if num + diff in num_set and num + 2 * diff in num_set:
            # If they are, increment the count
            count += 1
    
    # Return the count of triplets
    return count