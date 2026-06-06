def minimumAbsoluteDifference(arr):
    # First, we sort the array in ascending order
    arr.sort()

    # Initialize the minimum difference as infinity
    min_diff = float('inf')

    # Iterate over the sorted array to find the minimum difference
    for i in range(1, len(arr)):
        # Calculate the absolute difference between the current element and the previous element
        diff = abs(arr[i] - arr[i-1])
        
        # Update the minimum difference if the current difference is smaller
        if diff < min_diff:
            min_diff = diff

    # Return the minimum absolute difference
    return min_diff

# Test the function
arr = [4, 2, 1, 3]
print(minimumAbsoluteDifference(arr))  # Output: 1