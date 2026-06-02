def min_operations(nums, threshold, divisor):
    # Calculate the threshold value
    threshold_value = threshold // divisor
    
    # Initialize the count of operations
    operations = 0
    
    # Iterate over the list of numbers
    for num in nums:
        # If the number is greater than or equal to the threshold value
        if num >= threshold_value:
            # Increment the operations count by the difference between the number and the threshold value
            operations += num - threshold_value
    
    # Return the total operations count
    return operations