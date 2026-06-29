def minimumOperations(nums):
    # If the list is empty, return 0
    if not nums:
        return 0
    
    # Find the minimum number in the list
    # This is because we can subtract the minimum number from all other numbers to make them zero
    min_num = min(nums)
    
    # Initialize a variable to store the total number of operations
    total_operations = 0
    
    # Iterate over the list
    for num in nums:
        # For each number, subtract the minimum number and add the result to the total operations
        # We use the ceiling division operator (//) to round up to the nearest whole number
        # This is because we can't subtract a fraction of a number
        total_operations += (num - 1) // min_num + 1
    
    # Return the total number of operations
    return total_operations