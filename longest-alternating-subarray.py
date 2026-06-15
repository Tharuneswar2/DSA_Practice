def longestAlternatingSubarray(arr):
    # Initialize variables to store the maximum length and the current length
    max_length = 1
    current_length = 1
    
    # Iterate over the array from the second element to the end
    for i in range(1, len(arr)):
        # Check if the current element is greater than the previous element
        if arr[i] > arr[i - 1]:
            # If the current element is greater, check if the previous length was for a decreasing subarray
            if current_length > 1 and arr[i - 1] < arr[i - 2]:
                # If the previous length was for a decreasing subarray, update the current length
                current_length += 1
            else:
                # If the previous length was not for a decreasing subarray, reset the current length
                current_length = 2
        # Check if the current element is less than the previous element
        elif arr[i] < arr[i - 1]:
            # If the current element is less, check if the previous length was for an increasing subarray
            if current_length > 1 and arr[i - 1] > arr[i - 2]:
                # If the previous length was for an increasing subarray, update the current length
                current_length += 1
            else:
                # If the previous length was not for an increasing subarray, reset the current length
                current_length = 2
        # Update the maximum length
        max_length = max(max_length, current_length)
    
    # Return the maximum length
    return max_length

# Test the function
print(longestAlternatingSubarray([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))  # Output: 7
print(longestAlternatingSubarray([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: 2
print(longestAlternatingSubarray([9, 8, 7, 6, 5, 4, 3, 2, 1]))  # Output: 2