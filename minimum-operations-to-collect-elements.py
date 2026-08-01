# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def min_operations_to_collect_elements(arr):
    # Initialize variables to store the minimum operations and the current position
    min_operations = 0
    current_position = 0
    
    # Sort the array to group elements that need to be collected together
    arr.sort()
    
    # Iterate over the sorted array
    for i in range(len(arr)):
        # If this is not the first element and it's different from the previous one
        if i > 0 and arr[i] != arr[i-1]:
            # Update the current position to the previous element
            current_position = arr[i-1]
            # Increment the minimum operations by the difference between the current position and the previous element
            min_operations += arr[i] - current_position - 1
    
    # Return the minimum operations
    return min_operations