def valid_elements(arr, threshold):
    # Sort the array in ascending order
    arr.sort()
    
    # Initialize a variable to store the count of valid elements
    count = 0
    
    # Iterate over the sorted array
    for num in arr:
        # If the current number is less than or equal to the threshold, increment the count
        if num <= threshold:
            count += 1
        # If the current number exceeds the threshold, break the loop
        else:
            break
    
    # Return the count of valid elements
    return count

# Example usage:
arr = [1, 2, 3, 4, 5]
threshold = 3
print(valid_elements(arr, threshold))  # Output: 3