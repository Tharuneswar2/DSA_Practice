def longest_subarray(arr):
    # Initialize variables to store the maximum length and the current lengths of increasing and decreasing subarrays
    max_length = 1
    increasing = 1
    decreasing = 1

    # Iterate over the array from the second element to the end
    for i in range(1, len(arr)):
        # If the current element is greater than the previous one, increase the length of the increasing subarray
        if arr[i] > arr[i - 1]:
            increasing += 1
            # Reset the decreasing subarray length
            decreasing = 1
        # If the current element is less than the previous one, increase the length of the decreasing subarray
        elif arr[i] < arr[i - 1]:
            decreasing += 1
            # Reset the increasing subarray length
            increasing = 1
        # If the current element is equal to the previous one, reset both subarray lengths
        else:
            increasing = 1
            decreasing = 1
        # Update the maximum length
        max_length = max(max_length, increasing, decreasing)

    return max_length

# Test the function
print(longest_subarray([1, 2, 3, 4, 5]))  # Output: 5
print(longest_subarray([5, 4, 3, 2, 1]))  # Output: 5
print(longest_subarray([1, 3, 5, 7, 9, 8, 6, 4, 2]))  # Output: 6