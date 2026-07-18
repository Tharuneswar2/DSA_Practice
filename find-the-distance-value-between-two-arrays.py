# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def findTheDistanceValue(arr1, arr2, d):
    # Initialize a counter to store the number of elements in arr1 that are within the distance d from any element in arr2
    count = 0
    
    # Iterate over each element in arr1
    for num1 in arr1:
        # Initialize a flag to check if the current element in arr1 is within the distance d from any element in arr2
        is_within_distance = False
        
        # Iterate over each element in arr2
        for num2 in arr2:
            # Check if the absolute difference between the current elements in arr1 and arr2 is less than or equal to d
            if abs(num1 - num2) <= d:
                # If the condition is met, set the flag to True and break the loop
                is_within_distance = True
                break
        
        # If the flag is still False after the inner loop, it means the current element in arr1 is not within the distance d from any element in arr2
        if not is_within_distance:
            # Increment the counter
            count += 1
    
    # Return the count of elements in arr1 that are not within the distance d from any element in arr2
    return count