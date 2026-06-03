def maximize_expression(arr):
    # Initialize variables to store maximum values
    max_val = float('-inf')
    max_val_with_first = float('-inf')
    max_val_with_first_and_second = float('-inf')

    # Iterate over the array
    for i in range(len(arr)):
        # For each element, calculate the maximum value that can be obtained by 
        # multiplying it with the maximum value obtained so far and the maximum 
        # value obtained by multiplying the previous two elements
        max_val_with_first_and_second = max(max_val_with_first_and_second, 
                                            max_val_with_first * arr[i], 
                                            max_val * arr[i-1] * arr[i])
        
        # Update the maximum value obtained so far by multiplying the previous 
        # two elements
        max_val_with_first = max(max_val_with_first, max_val * arr[i])
        
        # Update the maximum value obtained so far
        max_val = max(max_val, arr[i])

    # Return the maximum value that can be obtained by multiplying three elements
    return max_val_with_first_and_second

# Test the function
arr = [1, 2, 3, 4]
print(maximize_expression(arr))