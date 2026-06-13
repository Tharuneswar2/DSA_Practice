def specialArray(nums):
    # Create a set of unique elements in the array
    unique_nums = set(nums)
    
    # Initialize the count of special elements
    special_count = 0
    
    # Iterate over the unique elements
    for num in unique_nums:
        # Check if the count of elements less than or equal to the current number is equal to the current number
        if sum(1 for x in nums if x <= num) == num:
            # If it is, increment the special count
            special_count += 1
    
    # If no special elements are found, return -1
    if special_count == 0:
        return -1
    # Otherwise, return the count of special elements
    else:
        return special_count