def getMinDiff(arr, n, k):
    # Sort the array in ascending order
    arr.sort()
    
    # Initialize the minimum difference
    min_diff = float('inf')
    
    # Iterate over the array to find the minimum difference
    for i in range(n - k + 1):
        # Calculate the difference between the maximum and minimum elements in the current window
        diff = arr[i + k - 1] - arr[i]
        
        # Update the minimum difference if the current difference is smaller
        min_diff = min(min_diff, diff)
    
    # Return the minimum difference
    return min_diff

# Test the function
arr = [1, 2, 3, 4, 5]
n = len(arr)
k = 3
print(getMinDiff(arr, n, k))