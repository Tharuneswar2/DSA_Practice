def minimumAbsoluteDifference(arr):
    # First, we sort the array in ascending order
    arr.sort()
    
    # Initialize the minimum difference with the difference between the first two elements
    min_diff = abs(arr[1] - arr[0])
    
    # Iterate over the array starting from the second element
    for i in range(1, len(arr) - 1):
        # Calculate the absolute difference between the current element and the next element
        diff = abs(arr[i + 1] - arr[i])
        
        # If the current difference is less than the minimum difference found so far, update the minimum difference
        if diff < min_diff:
            min_diff = diff
    
    # Return the minimum absolute difference found
    return min_diff

# Example usage:
arr = [4, 2, 1, 3]
print(minimumAbsoluteDifference(arr))  # Output: 1