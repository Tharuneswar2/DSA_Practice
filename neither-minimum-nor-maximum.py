def neither_min_nor_max(arr):
    # Check if the array has less than 3 elements
    if len(arr) < 3:
        return -1
    
    # Initialize minimum and maximum values
    min_val = min(arr)
    max_val = max(arr)
    
    # Iterate over the array to find the second minimum and second maximum values
    second_min = float('inf')
    second_max = float('-inf')
    for num in arr:
        if num < second_min and num != min_val:
            second_min = num
        if num > second_max and num != max_val:
            second_max = num
    
    # Check if second minimum and second maximum values exist
    if second_min == float('inf') or second_max == float('-inf'):
        return -1
    
    # Return the second minimum and second maximum values
    return second_min, second_max

# Test the function
arr = [1, 2, 3, 4, 5]
print(neither_min_nor_max(arr))