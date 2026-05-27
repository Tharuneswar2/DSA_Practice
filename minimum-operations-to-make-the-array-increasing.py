def minOperations(nums):
    # Initialize the count of operations
    operations = 0
    
    # Iterate over the array starting from the second element
    for i in range(1, len(nums)):
        # If the current element is not greater than the previous one
        if nums[i] <= nums[i - 1]:
            # Calculate the difference between the current element and the previous one plus one
            diff = nums[i - 1] - nums[i] + 1
            
            # Update the current element to be greater than the previous one
            nums[i] += diff
            
            # Increment the count of operations by the difference
            operations += diff
    
    # Return the total count of operations
    return operations