def count_hills_valleys(arr):
    # Initialize counters for hills and valleys
    hills = 0
    valleys = 0
    
    # Initialize a flag to track if we are currently in a hill or valley
    in_hill = False
    in_valley = False
    
    # Iterate over the array
    for i in range(1, len(arr)):
        # If the current element is greater than the previous one and we are not in a hill
        if arr[i] > arr[i-1] and not in_hill:
            # We are now in a hill
            in_hill = True
            in_valley = False
        # If the current element is less than the previous one and we are not in a valley
        elif arr[i] < arr[i-1] and not in_valley:
            # We are now in a valley
            in_valley = True
            in_hill = False
        # If the current element is greater than the previous one and we are in a valley
        elif arr[i] > arr[i-1] and in_valley:
            # We have just ended a valley
            valleys += 1
            in_valley = False
            in_hill = True
        # If the current element is less than the previous one and we are in a hill
        elif arr[i] < arr[i-1] and in_hill:
            # We have just ended a hill
            hills += 1
            in_hill = False
            in_valley = True
    
    # If the array ended in a hill or valley, count it
    if in_hill:
        hills += 1
    if in_valley:
        valleys += 1
    
    # Return the counts
    return hills, valleys

# Test the function
arr = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1]
hills, valleys = count_hills_valleys(arr)
print("Hills:", hills)
print("Valleys:", valleys)