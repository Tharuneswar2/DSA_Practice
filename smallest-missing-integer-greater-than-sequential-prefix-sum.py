def smallest_missing_integer(nums):
    # Create a set to store the numbers we've seen so far
    seen = set()
    
    # Initialize the smallest missing integer to 1
    smallest_missing = 1
    
    # Initialize the prefix sum to 0
    prefix_sum = 0
    
    # Iterate over the numbers in the list
    for num in nums:
        # Add the current number to the prefix sum
        prefix_sum += num
        
        # Add the current number to the set of seen numbers
        seen.add(num)
        
        # While the smallest missing integer is less than or equal to the prefix sum
        # and it's in the set of seen numbers, increment it
        while smallest_missing <= prefix_sum and smallest_missing in seen:
            smallest_missing += 1
    
    # Return the smallest missing integer
    return smallest_missing