def canMakeArithmeticProgression(arr):
    # First, we sort the array in ascending order
    arr.sort()
    
    # If the array has less than 2 elements, it can be an arithmetic progression
    if len(arr) < 2:
        return True
    
    # Calculate the common difference
    diff = arr[1] - arr[0]
    
    # Iterate over the array starting from the second element
    for i in range(2, len(arr)):
        # If the difference between the current element and the previous element is not equal to the common difference, return False
        if arr[i] - arr[i-1] != diff:
            return False
    
    # If we have checked all elements and haven't returned False, the array can be an arithmetic progression
    return True