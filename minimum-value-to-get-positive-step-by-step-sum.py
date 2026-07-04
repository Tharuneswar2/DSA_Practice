def minStartValue(nums):
    # Initialize the minimum value and the current sum
    min_val = 1
    curr_sum = 0
    
    # Iterate over the array
    for num in nums:
        # Update the current sum
        curr_sum += num
        
        # If the current sum is less than 1, update the minimum value
        if curr_sum < 1:
            min_val = max(min_val, 1 - curr_sum)
    
    # Return the minimum value
    return min_val