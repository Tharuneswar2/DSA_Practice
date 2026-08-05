# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def longest_subarray(arr):
    # Initialize variables to store the maximum length and the current lengths of increasing and decreasing subarrays
    max_length = 1
    increasing = 1
    decreasing = 1

    # Iterate over the array from the second element to the end
    for i in range(1, len(arr)):
        # Check if the current element is greater than the previous one
        if arr[i] > arr[i - 1]:
            # If it is, increase the length of the increasing subarray
            increasing += 1
            # Reset the length of the decreasing subarray
            decreasing = 1
        # Check if the current element is less than the previous one
        elif arr[i] < arr[i - 1]:
            # If it is, increase the length of the decreasing subarray
            decreasing += 1
            # Reset the length of the increasing subarray
            increasing = 1
        # If the current element is equal to the previous one, reset both lengths
        else:
            increasing = 1
            decreasing = 1
        
        # Update the maximum length
        max_length = max(max_length, increasing, decreasing)

    # Return the maximum length
    return max_length