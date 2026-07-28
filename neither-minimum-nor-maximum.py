# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def neither_min_nor_max(arr):
    # Check if the input array is empty
    if not arr:
        return -1
    
    # Find the minimum and maximum elements in the array
    min_val = min(arr)
    max_val = max(arr)
    
    # If the array contains only one unique element, return -1
    if min_val == max_val:
        return -1
    
    # Initialize a variable to store the result
    result = -1
    
    # Iterate through the array to find the first element that is neither min nor max
    for num in arr:
        # Check if the current number is neither min nor max
        if num != min_val and num != max_val:
            # Update the result and break the loop
            result = num
            break
    
    # Return the result
    return result