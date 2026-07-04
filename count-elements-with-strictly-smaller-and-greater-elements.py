def countElements(arr):
    # Sort the array in ascending order
    arr.sort()
    
    # Initialize variables to store the count of elements with strictly smaller and greater elements
    count = 0
    
    # Iterate over the array
    for i in range(len(arr)):
        # Check if the current element is not the smallest and not the largest
        if arr[0] < arr[i] < arr[-1]:
            # If the condition is met, increment the count
            count += 1
    
    # Return the count
    return count

# Test the function
print(countElements([11, 7, 2, 15]))  # Output: 2
print(countElements([1, 2, 3, 4, 5]))  # Output: 3