# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def countElements(arr):
    # Sort the array in ascending order
    arr.sort()
    
    # Initialize variables to store the count of elements with strictly smaller and greater elements
    count = 0
    
    # Iterate over the sorted array
    for i in range(len(arr)):
        # Check if the current element is not the smallest and not the largest
        if arr[0] < arr[i] < arr[-1]:
            # If the condition is met, increment the count
            count += 1
    
    # Return the count of elements with strictly smaller and greater elements
    return count