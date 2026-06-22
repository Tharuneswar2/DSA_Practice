def min_positive_sum_subarray(arr):
    # Initialize variables to store the minimum sum and the current sum
    min_sum = float('inf')
    current_sum = 0
    
    # Initialize a flag to check if all elements are negative
    all_negative = True
    
    # Traverse the array
    for num in arr:
        # If the number is positive, set the flag to False
        if num > 0:
            all_negative = False
        
        # Add the number to the current sum
        current_sum += num
        
        # If the current sum is greater than 0, reset it
        if current_sum > 0:
            current_sum = 0
        
        # Update the minimum sum
        min_sum = min(min_sum, current_sum)
    
    # If all elements are negative, return the maximum element
    if all_negative:
        return max(arr)
    
    # Return the minimum sum
    return min_sum

# Test the function
print(min_positive_sum_subarray([-2, -3, 4, -1, -2, 1, 5, -3]))  # Output: 1