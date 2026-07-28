# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def minimumAbsDifference(arr):
    # First, sort the array in ascending order
    arr.sort()
    
    # Initialize the minimum difference and the result list
    min_diff = float('inf')  # Initialize with positive infinity
    result = []
    
    # Iterate through the sorted array to find the minimum difference
    for i in range(1, len(arr)):
        # Calculate the absolute difference between the current element and the previous element
        diff = abs(arr[i] - arr[i-1])
        
        # If the current difference is less than the minimum difference found so far, update the minimum difference and reset the result list
        if diff < min_diff:
            min_diff = diff
            result = [[arr[i-1], arr[i]]]
        # If the current difference is equal to the minimum difference found so far, add the pair to the result list
        elif diff == min_diff:
            result.append([arr[i-1], arr[i]])
    
    # Return the result list containing all pairs with the minimum absolute difference
    return result